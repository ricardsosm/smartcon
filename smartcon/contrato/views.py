from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import permition_required
from cliente.models import Cliente
from .models import Contrato
from carteira.models import Carteira
from .forms import ContratoNovoForm, EditarContrato
from itertools import chain
from .arquivo import Grava

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
		Grava(request)
		if form.is_valid():
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
		Grava(request)
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