from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import permition_required
from cliente.models import Cliente
from .models import Contrato
from carteira.models import Carteira
from .forms import ContratoNovoForm, EditarContrato,MostrarContrato,PublicarContrato
from itertools import chain
from .arquivo import Grava, Apaga
from .fabrica import Fabrica
from web3 import Web3
import json

@login_required
def contrato(request):
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)
	contrato = []
	for cli in cliente:
		contrato = list(chain(contrato, Contrato.objects.all().filter(id_cliente = cli.id)))

	template_name = 'contrato.html'
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
def contrato_novo(request):
	template_name = 'contrato_register.html'
	cliente = Cliente.objects.filter(id_usuario = request.user.id)
	carteira = []
	for cli in cliente:
		carteira = list(chain(carteira, Carteira.objects.all().filter(id_cliente = cli.id)))

	if request.method == 'POST':
		form = ContratoNovoForm(request.POST,user=request.user.id)
		if form.is_valid():
			Grava(request)
			form.save()
			messages.success(request,"Contrato criado com sucesso",extra_tags='text-success')
			return redirect('con:contrato')
	else:
		form = ContratoNovoForm(user=request.user.id)	
	context = {
		'form': form,
		'cliente': cliente,
		'carteira': carteira
	}
	return render(request, template_name, context)

@login_required
def contrato_pesquisa(request):
	template_name = 'contrato.html'
	contrato = Contrato.objects.all().filter(name__icontains=pesquisa)

@login_required
@permition_required
def contrato_apaga(request,pk):
	contrato = Contrato.objects.get(pk=pk)
	Apaga(contrato)
	contrato.delete()
	messages.success(request,"Contrato apagado com sucesso",extra_tags='text-success')
	return redirect('con:contrato')

@login_required
@permition_required
def contrato_editar(request,pk):
	template_name = 'contrato_editar.html'
	contrato = Contrato.objects.get(pk=pk)
	if request.method == 'POST':
		form = EditarContrato(request.POST or None, instance=contrato)
		if form.is_valid():
			form.save()
			messages.success(request,"Contrato salvo com sucesso",extra_tags='text-success')
		redirect('con:contrato')		
	else:
		form = EditarContrato(instance=contrato)
	context = {
		'form': form
	}
	return render(request, template_name, context)

@login_required
@permition_required
def contrato_mostrar(request,pk):
	template_name = 'contrato_mostrar.html'
	contrato = Contrato.objects.get(pk=pk)
	form = MostrarContrato(instance=contrato)
	if request.method == 'POST':
		return redirect('con:contrato')
	context = {
		'form': form
	}
	return render(request, template_name, context)

@login_required
@permition_required
def contrato_puclicar(request,pk):
	template_name = 'contrato_publicar.html'
	contrato = Contrato.objects.get(pk=pk)
	if contrato.ativo == True:
		messages.success(request,"Este contrato ja esta publicado",extra_tags='text-danger')
		return redirect('con:contrato')
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)
	form = PublicarContrato(instance=contrato)
	if request.method == 'POST':
		request.POST = request.POST.copy()
		path = 'contract/'+str(contrato.id_cliente.id) +'/'+contrato.name+'.sol'
		fab = Fabrica(path,contrato.wallet_private_key)
		numcontrato = fab.enviar()	
		g = str(numcontrato)
		if g[0] == 'b':
			contratonum = Web3.toHex(numcontrato)
			request.POST.update({'abi':fab.abi})
			request.POST.update({'ativo':'True'})
			request.POST.update({'contract_address':contratonum})			
			form = PublicarContrato(request.POST or None, instance=contrato)	
			if form.is_valid():							
				form.save()
				messages.success(request,"Contrato Publicado com sucesso",extra_tags='text-success')
				return redirect('con:contrato')
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