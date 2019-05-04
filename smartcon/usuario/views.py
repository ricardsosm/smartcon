from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from cliente.models import Cliente
from .forms import EditarConta, PasswordResetForm, ApagarConta
from .models import PasswordReset
from .decorators import user_permition_required

User = get_user_model()

@login_required
def editar(request):
	template_name = 'editar.html'
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)

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
	context['cliente'] = cliente
	return render(request, template_name,context)

@login_required
def edit_password(request):
	template_name = 'edit_password.html'
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)
	context = {}
	if request.method ==  'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			context['success'] = True
	else:
		form = PasswordChangeForm(user=request.user)
	context['form'] = form
	context['cliente'] = cliente
	return render(request,template_name,context)

def password_reset(request):
	context ={}
	template_name = "password_reset.html"
	form = PasswordResetForm(request.POST or None)
	if form.is_valid():
		form.save()
		context['success'] = True
	context['form'] = form
	return render(request, template_name,context)

def password_reset_confirm(request,key):
	template_name = 'password_reset_confirm.html'
	context = {}
	reset = get_object_or_404(PasswordReset,key=key)
	form = SetPasswordForm(user=reset.user, data=request.POST or None)
	if form.is_valid():
		form.save()
		context['success'] = True
	context['form'] = form
	return render(request, template_name,context)

@login_required
@user_permition_required
def usuario_apagar(request,pk):
	template_name = 'usuario_apagar.html'
	return render(request, template_name)

@login_required
@user_permition_required
def usuario_del(request,pk):
	user = User.objects.get(pk=pk)
	user.delete()
	return redirect('sis:logout')