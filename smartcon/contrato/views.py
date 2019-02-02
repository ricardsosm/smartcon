from django.shortcuts import render, redirect, get_object_or_404
from cliente.models import Cliente
from .models import Contrato
from .forms import ContratoNovoForm

def contrato(request):
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)
	contrato = Contrato.objects.all()
	template_name = 'contrato.html'
	context = {
		'cliente':cliente,
		'contrato': contrato
	}
	return render(request, template_name,context)

def contrato_novo(request):
	template_name = 'contrato_register.html'
	cliente = Cliente.objects.filter(id_usuario = request.user.id)
	context = {}
	if request.method == 'POST':
		form = ContratoNovoForm(request.POST,user=request.user.id)
		print(request.POST)
		if form.is_valid():
			form.save()
			return redirect('con:contrato')
	else:
		form = ContratoNovoForm(user=request.user.id)	
	context = {
		'form': form,
		'cliente': cliente
	}
	return render(request, template_name, context)
