from django import forms
from .models import Carteira, CarteiraToken
from cliente.models import Cliente
from eth_account import Account
from web3 import Web3
import random

class MostrarCarteira(forms.ModelForm):

	name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
	saldo = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','id':'id_saldo_carteira'}))
	public_key = forms.CharField(label='Chave Pública',widget=forms.TextInput(attrs={'readonly':'True'}))
	public_key.widget.attrs.update({'size':'42'})  
	private_key = forms.CharField(label='Chave Privada',widget=forms.TextInput(attrs={'readonly':'True','type':'password'}))
	private_key.widget.attrs.update({'size':'56','action':'hide'}) 

	class Meta:
		model = Carteira
		fields = ['name','saldo','public_key','private_key']

class CarteiraNovaForm(forms.ModelForm):

	conta = Account.create(random.randint(1, 999999999))

	name = forms.CharField(label='Nome',widget=forms.TextInput(attrs={'size':'20'}))	
	public_key = forms.CharField(label='Chave Pública',widget=forms.TextInput(attrs={'value':conta.address}))
	public_key.widget.attrs.update({'size':'42'}) 
	key = Web3.toHex(conta.privateKey)
	private_key = forms.CharField(label='Chave Privada',widget=forms.TextInput(attrs={'value':key,'type':'password'}))
	private_key.widget.attrs.update({'size':'56','action':'hide'}) 

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user','')
		super(CarteiraNovaForm, self).__init__(*args, **kwargs)

		self.fields['id_cliente']=forms.ModelChoiceField(
			label='Cliente',
			queryset=Cliente.objects.filter(id_usuario=user)
		)

	class Meta:
		model = Carteira
		fields = ['name','id_cliente','public_key','private_key']

class NovoTokenForm(forms.ModelForm):

	class Meta:
		model = CarteiraToken
		fields = ['token','simbolo','saldo','id_carteira']