from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import permition_conrequired
from cliente.models import Cliente
from .models import Contrato, ContratActions,ContratToken
from carteira.models import Carteira, CarteiraToken
from .forms import ContratoNovoForm, EditarContrato,MostrarContrato,PublicarContrato
from itertools import chain 
from .arquivo import Token, Apaga, GravaAbi
from .fabrica import Fabrica
from web3 import Web3, HTTPProvider
from eth_account import Account
from django.conf import settings
import json, time

@login_required
def contrato(request):
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)
	template_name = 'contrato.html'
	context = {
		'cliente':cliente,
	}
	return render(request, template_name,context)

@login_required
def contrato_listar(request):
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)
	contrato = []
	for cli in cliente:
		contrato = list(chain(contrato, Contrato.objects.all().filter(id_cliente = cli.id)))

	template_name = 'contrato_listar.html'
	pesquisa =''
	if request.method == 'POST':
		pesquisa = request.POST.get("pescli")
		contrato = Contrato.objects.all().filter(name__icontains=pesquisa)
	context = {
		'cliente':cliente,
		'contrato': contrato
	}
	return render(request, template_name,context)


@login_required
def contrato_pesquisa(request):
	template_name = 'contrato.html'
	contrato = Contrato.objects.all().filter(name__icontains=pesquisa)

@login_required
@permition_conrequired
def contrato_apaga(request,pk):
	contrato = Contrato.objects.get(pk=pk)
	contrato_token = ContratToken.objects.filter(id_contrato_id = contrato.id)
	Apaga(contrato)
	contrato_token.delete()
	contrato.delete()

	messages.success(request,"Contrato apagado com sucesso",extra_tags='text-success')
	return redirect('con:contrato_listar')

@login_required
@permition_conrequired
def contrato_editar(request,pk):
	template_name = 'contrato_editar.html'
	contrato = Contrato.objects.get(pk=pk)
	if contrato.ativo == True:
		messages.success(request,"Este contrato não pode mais ser editado",extra_tags='text-danger')
		return redirect('con:contrato_listar')

	if request.method == 'POST':
		form = EditarContrato(request.POST or None, instance=contrato)
		if form.is_valid():
			form.save()
			messages.success(request,"Contrato salvo com sucesso",extra_tags='text-success')
		return redirect('con:contrato_listar')		
	else:
		form = EditarContrato(instance=contrato)
	context = {
		'form': form
	}
	return render(request, template_name, context)

@login_required
@permition_conrequired
def contrato_mostrar(request,pk):
	template_name = 'contrato_mostrar.html'
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)
	contrato = Contrato.objects.get(pk=pk)
	try:
		action = ContratActions.objects.get(id_contrato = pk)
	except:
		action = None
	if request.method == 'POST':
		return redirect('con:contrato_listar')

	w3 = Web3(HTTPProvider(settings.PROVEDOR))
	cona = ContratActions.objects.get(id_contrato = contrato.pk)
	conadress = cona.contract_address
	myContract = w3.eth.contract(address=conadress, abi=contrato.abi)
	#one = myContract.functions.getCount().call()
	one = 'none'

	context = {
		'cliente':cliente,
		'contrato':contrato,
		'recibo': action,
		'conta': one
	}

	return render(request, template_name, context)

@login_required
@permition_conrequired
def contrato_puclicar(request,pk):
	template_name = 'contrato_publicar.html'
	contrato = Contrato.objects.get(pk=pk)
	if contrato.ativo == True:
		messages.success(request,"Este contrato ja esta publicado",extra_tags='text-danger')
		return redirect('con:contrato_listar')
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)
	form = PublicarContrato(instance=contrato)
	carteira = Carteira.objects.get(pk=contrato.id_carteira)
	token = ContratToken.objects.get(id_contrato_id=contrato.id)
	if request.method == 'POST':
		request.POST = request.POST.copy()
		path = 'contract/'+str(contrato.id_cliente.id) +'/'+contrato.name+'.sol'
		fab = Fabrica(path,carteira.private_key)
		numcontrato = fab.enviar()	
		g = str(numcontrato)
		if g[0] == 'b':
			contratonum = Web3.toHex(numcontrato)		
			form = PublicarContrato(request.POST or None, instance=contrato)	
			if form.is_valid():							
				contrato.hash_address = contratonum 
				contrato.abi = json.dumps(fab.myabi)
				contrato.ativo = False
				contrato.save()

				carToken = CarteiraToken()
				carToken.id_token = token.id
				carToken.token = token.token
				carToken.simbolo = token.simbolo
				carToken.id_carteira = Carteira.objects.get(pk=carteira.id)
				carToken.save()

				return redirect('con:valrecibo', pk)
			else:
				messages.success(request,"Erro de validação",extra_tags='text-danger')		
		else:
			g = g.replace("\'", "\"")
			j = json.loads(g)
			if (j.get("code")) == -32000:
				messages.success(request,"Voce não tem saldo suficiente",extra_tags='text-danger')

	context = {
		'form': form,
		'cliente': cliente,
	}
	return render(request, template_name, context)

@login_required
@permition_conrequired
def recibo(request,pk):
	template_name = 'recibo.html'
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)
	contrato = Contrato.objects.get(pk=pk)
	w3 = Web3(HTTPProvider(settings.PROVEDOR))
	while True:
		recibo = w3.eth.getTransactionReceipt(contrato.hash_address)
		if recibo:
			if contrato.ativo == False:
				action = ContratActions()
				action.blocknumber = recibo["blockNumber"]
				action.status = recibo["status"]
				action.contract_address = recibo["contractAddress"]
				action.from_adress = recibo["from"]
				action.to_adress = recibo["to"]
				transhash = recibo["transactionHash"]
				action.transactionHash = Web3.toHex(transhash)
				action.gasUsed = recibo["gasUsed"]
				action.id_contrato = Contrato.objects.get(pk=pk)
				action.save()
				contrato.contract_address = recibo["contractAddress"]
				contrato.ativo = True
				contrato.save()
				messages.success(request,"Contrato Publicado com sucesso",extra_tags='text-success')
				break
			else:
				break
		time.sleep(1)
	
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)

	context = {
		'cliente':cliente,
		'contrato': contrato,
		'cliente':cliente,
		'recibo': recibo,
	}
	return render(request, template_name, context)

@login_required
@permition_conrequired
def valrecibo(request,pk):
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)
	contrato = Contrato.objects.get(pk=pk)
	if contrato.ativo == None:
		messages.success(request,"Voce precisa Publicar o Comtrato antes",extra_tags='text-danger')
		return redirect('con:contrato_listar')
	template_name = 'valida_recibo.html'
	context = {
		'pk': pk,
		'cliente': cliente
	}
	return render(request, template_name, context)

@login_required
@permition_conrequired
def contrato_interar(request,pk):
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)
	contrato = Contrato.objects.get(pk=pk)
	action = ContratActions.objects.all().filter(id_contrato = contrato.id)
	template_name = 'contrato_interar.html'
	context = {
		'contrato': contrato,
		'action': action,
		'cliente':cliente
	}
	return render(request, template_name, context)

@login_required
def contrato_token(request):
	template_name = 'contrato_token.html'
	cliente = Cliente.objects.filter(id_usuario = request.user.id)
	carteira = []
	for cli in cliente:
		carteira = list(chain(carteira, Carteira.objects.all().filter(id_cliente = cli.id)))

	if request.method == 'POST':
		form = ContratoNovoForm(request.POST,user=request.user.id)
		if form.is_valid():
			cart = request.POST.get("id_carteira")
			carte = Carteira.objects.get(pk=cart)
			Token(request, carte.public_key)
			form.save()
			token = ContratToken()		
			token.token = request.POST.get("token")
			token.simbolo = request.POST.get("simbolo")
			token.quantidade = request.POST.get("qtde")
			token.digitos = request.POST.get("digitos")
			token.id_contrato = Contrato.objects.get(pk=form.instance.id)
			token.save()

			messages.success(request,"Contrato criado com sucesso",extra_tags='text-success')
			return redirect('con:contrato_listar')
	else:
		form = ContratoNovoForm(user=request.user.id)	
	context = {
		'form':form,
		'cliente': cliente,
		'carteira': carteira
	}
	return render(request, template_name, context)
