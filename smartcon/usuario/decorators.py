from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario

def user_permition_required(view_func):
	def _wrapper(request, *args,**kwargs):
		has_permition = False
		pk = kwargs['pk']
		if request.user.pk == pk:
			has_permition = True

		if not has_permition:
			message = 'Desculpe, mas voce não tem permissão'
			messages.error(request,message)
			return redirect('sis:painel')
		return view_func(request, *args,**kwargs)
	return _wrapper