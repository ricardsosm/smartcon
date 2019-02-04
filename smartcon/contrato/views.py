from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import permition_required
from cliente.models import Cliente
from .models import Contrato
from .forms import ContratoNovoForm
from itertools import chain

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
	if request.method == 'POST':
		form = ContratoNovoForm(request.POST,user=request.user.id)
		print(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,"Contrato criado com sucesso",extra_tags='text-success')
			return redirect('con:contrato')
	else:
		form = ContratoNovoForm(user=request.user.id)	
	context = {
		'form': form,
		'cliente': cliente
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