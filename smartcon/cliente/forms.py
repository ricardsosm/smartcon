from django import forms
from sistema.mail import send_mail_template
from .models  import Cliente
from usuario.models import Usuario
from carteira.models import Carteira
from eth_account import Account
import random


class ClienteNovoForm(forms.ModelForm):

	name = forms.CharField(label='Nome',widget=forms.TextInput(attrs={'placeholder':'Digite seu Nome'}))
	name.widget.attrs.update({'size':'21'}) 
	cpf = forms.CharField(label='CPF',widget=forms.TextInput(attrs={'placeholder':'Digite seu CPF'}))
	tel = forms.CharField(label='Telefone',widget=forms.TextInput(attrs={'placeholder':'Digite seu Telefone','class':'tel'}))  
	id_usuario = forms.ModelChoiceField(
		queryset=Usuario.objects.all(),
		widget=forms.HiddenInput(),
		label='',
	)

	class Meta:
		model = Cliente
		fields = ['name','cpf','tel','id_usuario']

class EditarCliente(forms.ModelForm):

	name = forms.CharField(label='Nome')
	name.widget.attrs.update({'size':'25'}) 
	cpf = forms.CharField(label='CPF',widget=forms.TextInput(attrs={'class':'cpf'}))
	tel = forms.CharField(label='Telefone',widget=forms.TextInput(attrs={'class':'tel'})) 


	class Meta:
		model = Cliente
		fields = ['name','cpf','tel']

class MostrarCliente(forms.ModelForm):

	name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
	cpf = forms.CharField(label='CPF',widget=forms.TextInput(attrs={'class':'cpf','readonly':'True'}))
	tel = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))


	class Meta:
		model = Cliente
		fields = ['name','cpf','tel']


class MostrarCarteira(forms.ModelForm):

	name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
	saldo = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','id':'id_saldo_carteira'}))
	public_key = forms.CharField(label='Chave Pública',widget=forms.TextInput(attrs={'readonly':'True'}))
	public_key.widget.attrs.update({'size':'42'})  
	private_key = forms.CharField(label='Chave Privada',widget=forms.TextInput(attrs={'readonly':'True'}))
	private_key.widget.attrs.update({'size':'60'}) 

	class Meta:
		model = Carteira
		fields = ['name','saldo','public_key','private_key']

class CarteiraNovaForm(forms.ModelForm):

	name = forms.CharField(label='Nome',widget=forms.TextInput(attrs={'size':'20'}))	
	conta = Account.create(random.randint(1, 999999999))
	public_key = forms.CharField(label='Chave Pública',widget=forms.TextInput(attrs={'value':conta.address}))
	public_key.widget.attrs.update({'size':'42'}) 
	private_key = forms.CharField(label='Chave Privada',widget=forms.TextInput(attrs={'value':conta.privateKey}))
	private_key.widget.attrs.update({'size':'60'}) 

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




