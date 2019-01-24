from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import ClienteNovoForm, EditarCliente, MostrarCliente
from .models  import Cliente
from .decorators import permition_required

User = get_user_model()

@login_required	
def cliente(request):
	cliente = Cliente.objects.filter(id_usuario=request.user.pk)
	template_name = 'cliente.html'
	context = {
		'clientes': cliente
	}
	return render(request, template_name, context)

@login_required
def cliente_novo(request):
	template_name = 'cliente_register.html'
	context = {}
	if request.method == 'POST':
		form = ClienteNovoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('cli:cliente')
	else:
		form = ClienteNovoForm(
			initial={'id_usuario': request.user},
		)	
	context = {
		'form': form,
	}
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
			form = EditarCliente(instance=cliente)
			context['success'] = True
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