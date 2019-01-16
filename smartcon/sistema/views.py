from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from .forms import RegisterForm
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

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
	return render(request, template_name,context)
	