from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ClienteNovoForm, EditarCliente, MostrarCliente, MostrarCarteira,CarteiraNovaForm
from .models  import Cliente
from contrato.models import ContratActions, ContratToken
from carteira.models import Carteira, CarteiraToken
from .decorators import permition_required
from django.contrib import messages
from eth_account import Account
from itertools import chain
from web3 import Web3, HTTPProvider
from django.conf import settings

@login_required	
def cliente(request):
	cliente = Cliente.objects.filter(id_usuario=request.user.pk)
	template_name = 'cliente.html'
	pesquisa =''
	if request.method == 'POST':
		pesquisa = request.POST.get("pescli")
		cliente = Cliente.objects.filter(id_usuario=request.user.pk).filter(name__icontains=pesquisa)
	context = {
		'clientes': cliente
	}		
	return render(request, template_name, context)

@login_required
def cliente_novo(request):
	context = {}
	template_name = 'cliente_register.html'
	if request.method == 'POST':
		form = ClienteNovoForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,"Cliente cadastrado com sucesso",extra_tags='text-success')
			return redirect('cli:cliente')
	else:
		form = ClienteNovoForm(
			initial={'id_usuario': request.user},
		)	
	context['form'] = form
	return render(request, template_name, context)

@login_required
@permition_required
def cliente_editar(request,pk):
	template_name = 'cliente_editar.html'
	cliente = Cliente.objects.get(pk=pk)
	context = {}
	if request.method == 'POST':
		form = EditarCliente(request.POST or None, instance=cliente)
		if form.is_valid():
			form.save()
			messages.success(request,"Cliente salvo com sucesso",extra_tags='text-success')
			return redirect('cli:cliente')
		else:messages.success(request,"Erro",extra_tags='text-danger')
	else:
		form = EditarCliente(instance=cliente)
	context['form'] = form
	return render(request, template_name, context)			

@login_required
@permition_required
def cliente_mostrar(request,pk):
	template_name = 'cliente_mostrar.html'
	cliente = Cliente.objects.get(pk=pk)
	context = {}
	form = MostrarCliente(instance=cliente)
	if request.method == 'POST':
		return redirect('cli:cliente')
	context['form'] = form
	return render(request, template_name, context)

@login_required
@permition_required
def cliente_apagar(request,pk):
	cliente = Cliente.objects.get(pk=pk)
	cliente.delete()
	messages.success(request,"Cliente apagado com sucesso",extra_tags='text-success')
	return redirect('cli:cliente')

@login_required
def cliente_pesquisa(request):
	template_name = 'cliente.html'
	context = {}
	cliente = Cliente.objects.filter(id_usuario=request.user.pk)

@login_required
def carteira_mostrar(request):
	template_name = 'carteira_mostrar.html'
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)
	carteira  = []
	for cli in cliente:
		carteira = list(chain(carteira , Carteira .objects.all().filter(id_cliente = cli.id)))

	context = {}
	form = MostrarCarteira()
	if request.method == 'POST':
		pesquisa = request.POST.get("pescli")
		carteira = Carteira.objects.all().filter(name__icontains=pesquisa)
	context['carteiras'] = carteira
	return render(request, template_name, context)

@login_required
def carteira_gerar(request):
	template_name = 'carteira_gerar.html'
	context = {}
	if request.method == 'POST':
		form = CarteiraNovaForm(request.POST,user=request.user.id)
		if form.is_valid():
			form.save()
			messages.success(request,"Carteira gerada com sucesso",extra_tags='text-success')
			return redirect('cli:carteira')	
		else:messages.success(request,"Erro ao gerar carteira",extra_tags='text-danger')

	form = CarteiraNovaForm(user=request.user.id)
	context['form'] = form
	return render(request, template_name, context)

@login_required
def carteira_apagar(request,pk):
	carteira = Carteira.objects.get(pk=pk)
	carteira.delete()
	messages.success(request,"Carteira apagado com sucesso",extra_tags='text-success')
	return redirect('cli:carteira')

@login_required
def carteira_amostra(request,pk):
	template_name = 'carteira_amostra.html'
	carteira = Carteira.objects.get(pk=pk)
	tokens = CarteiraToken.objects.filter(id_carteira=carteira.id)

	#contrato = Contrato.objects.get(pk=tokens.id_contrato)

	w3 = Web3(HTTPProvider(settings.PROVEDOR))
	bal = w3.eth.getBalance(carteira.public_key)
	for token in tokens:
		print(token.contract_address)
		#erc20 = w3.eth.contract(address=address,abi=abi)
	carteira.saldo = bal
	form = MostrarCarteira(instance=carteira)
	context = {
		'form': form,
		'tokens': tokens
	}
	return render(request, template_name, context)