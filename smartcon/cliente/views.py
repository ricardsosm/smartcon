from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import EditarConta, PasswordResetForm

@login_required
def painel(request):
	template_name = 'painel.html'
	context = {}
	return render(request, template_name,context)

@login_required
def contrato(request):
	template_name = 'contrato.html'
	context = {}
	return render(request, template_name,context)

@login_required
def editar(request):
	template_name = 'editar.html'
	context = {}
	if request.method == 'POST':
		form = EditarConta(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			form = EditarConta(instance=request.user)
			context['success'] = True
	else:
		form = EditarConta(instance=request.user)
	context['form'] = form
	return render(request, template_name,context)	