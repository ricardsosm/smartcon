from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import ClienteNovoForm
from .models  import Cliente

User = get_user_model()

@login_required	
def cliente(request):
	cliente = Cliente.objects.all()
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
			context['success']=True
			return redirect('cli:cliente')
	else:
		form = ClienteNovoForm(
			initial={'id_usuario': request.user},
		)	
	context = {
		'form': form,
	}
	return render(request, template_name, context)

