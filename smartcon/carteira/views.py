from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from contrato.models import Contrato, ContratActions, ContratToken
from .forms import MostrarCarteira,CarteiraNovaForm
from .models import Carteira, CarteiraToken
from cliente.models import Cliente
from django.contrib import messages
from eth_account import Account
from itertools import chain
from web3 import Web3, HTTPProvider
from django.conf import settings

@login_required
def carteira_mostrar(request):
	template_name = 'carteira_mostrar.html'
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)
	carteira  = []
	for cli in cliente:
		carteira = list(chain(carteira , Carteira .objects.all().filter(id_cliente = cli.id)))

	context = {}
	form = MostrarCarteira()
	if request.method == 'POST':
		pesquisa = request.POST.get("pescli")
		carteira = Carteira.objects.all().filter(name__icontains=pesquisa)
	context['carteiras'] = carteira
	return render(request, template_name, context)

@login_required
def carteira_gerar(request):
	template_name = 'carteira_gerar.html'
	context = {}
	if request.method == 'POST':
		form = CarteiraNovaForm(request.POST,user=request.user.id)
		if form.is_valid():
			form.save()
			messages.success(request,"Carteira gerada com sucesso",extra_tags='text-success')
			return redirect('car:carteira')	
		else:messages.success(request,"Erro ao gerar carteira",extra_tags='text-danger')

	form = CarteiraNovaForm(user=request.user.id)
	context['form'] = form
	return render(request, template_name, context)

@login_required
def carteira_apagar(request,pk):
	carteira = Carteira.objects.get(pk=pk)
	carteira.delete()
	messages.success(request,"Carteira apagado com sucesso",extra_tags='text-success')
	return redirect('car:carteira')

@login_required
def carteira_amostra(request,pk):
	template_name = 'carteira_amostra.html'
	carteira = Carteira.objects.get(pk=pk)
	tokens = []
	contrato = []
	saldo = []
	tok = CarteiraToken.objects.filter(id_carteira=carteira.id)
	w3 = Web3(HTTPProvider(settings.PROVEDOR))
	bal = w3.eth.getBalance(carteira.public_key)	
	if tok:
		for tk in tok:
			tokens = ContratToken.objects.filter(pk = tk.id_token)
			for token in tokens:
				contrato = Contrato.objects.filter(id = token.id_contrato_id)
				for con in contrato:
					if con.contract_address:
						erc20 = w3.eth.contract(address=con.contract_address,abi=con.abi)
						tk.saldo = erc20.functions.balanceOf(carteira.public_key).call()


	carteira.saldo = bal
	form = MostrarCarteira(instance=carteira)
	context = {
		'form': form,
		'tok': tok
	}
	return render(request, template_name, context)