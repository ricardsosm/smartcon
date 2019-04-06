from django import forms
from sistema.mail import send_mail_template
from .models  import Cliente
from usuario.models import Usuario
from carteira.models import Carteira
from eth_account import Account
from web3 import Web3
import random


class ClienteNovoForm(forms.ModelForm):

	name = forms.CharField(label='Nome',widget=forms.TextInput(attrs={'placeholder':'Digite seu Nome'}))
	name.widget.attrs.update({'size':'25'}) 
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
	name.widget.attrs.update({'size':'25'}) 
	cpf = forms.CharField(label='CPF',widget=forms.TextInput(attrs={'class':'cpf','readonly':'True'}))
	tel = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))


	class Meta:
		model = Cliente
		fields = ['name','cpf','tel']

