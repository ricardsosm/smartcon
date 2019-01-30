from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from cliente.models import Cliente
from django.conf import settings

User = get_user_model()

def home(request):
	return render(request,'home.html')

def login(request):
	return render(request,'login.html')

def register(request):
	template_name = 'register.html'
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(settings.LOGIN_URL)
	else:
		form = RegisterForm()		
	context = {
		'form': form,
	}
	return render(request, template_name, context)

@login_required
def ip_cliente(request):
	ip = request.META.get('X_FORWARDED_FOR')
	if ip is None:
		ip = request.META.get('REMOTE_ADDR')
	user = User.objects.get(id = request.user.pk)
	user.ip_last = user.ip_actual
	user.ip_actual = ip
	user.save()
	return redirect('sis:painel') 


@login_required
def painel(request):
	cliente = Cliente.objects.filter(id_usuario=request.user.pk)
	template_name = 'painel.html'
	context = {
		'cliente':cliente
	}
	return render(request, template_name,context)

@login_required
def contrato(request):
	template_name = 'contrato.html'
	context = {}
	return render(request, template_name,context)
	