from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario
from cliente.models import Cliente

def user_permition_required(view_func):
	def _wrapper(request, *args,**kwargs):
		has_permition = False
		pk = kwargs['pk']
		if request.user.pk == pk:
			cliente = Cliente.objects.filter(id_usuario=request.user.pk)
			if cliente.count() == 0:
				has_permition = True
			else:
				message = 'apague os Clientes antes de excluir a conta'
				messages.error(request,message)
				return redirect('sis:painel')

		if not has_permition:
			message = 'Desculpe, mas voce não tem permissão'
			messages.error(request,message)
			return redirect('sis:painel')
		return view_func(request, *args,**kwargs)
	return _wrapper