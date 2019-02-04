from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from cliente.models import Cliente
from .models import Contrato

def permition_required(view_func):
	def _wrapper(request, *args,**kwargs):
		pk = kwargs['pk']
		contrato = get_object_or_404(Contrato,pk=pk)
		pkcon = contrato.id_cliente.id
		cliente = get_object_or_404(Cliente,pk=contrato.id_cliente.id)
		has_permition = request.user.is_staff
		if not has_permition:
			try:
				contrato = Contrato.objects.get(
					id_cliente=pkcon,
					pk=pk
				)
			except cliente.DoesNotExist:
				messages.success(request,'Desculpe, mas voce não tem permissão',extra_tags='text-denger')
			else:
				has_permition = True

		if not has_permition:
			messages.error(request,message)
			return redirect('con:contrato')
		request.contrato = contrato
		return view_func(request, *args,**kwargs)
	return _wrapper