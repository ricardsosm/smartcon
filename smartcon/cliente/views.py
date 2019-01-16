from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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