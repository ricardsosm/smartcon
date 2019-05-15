from django import forms
from django.forms.models import modelformset_factory
from sistema.mail import send_mail_template
from .models import Contrato, ContratActions
from carteira.models import Carteira
from cliente.models  import Cliente
from django.forms import modelformset_factory
from django.contrib.auth import get_user_model
from itertools import chain 

User = get_user_model()

class ContratoNovoForm(forms.ModelForm):

	name = forms.CharField(label='Nome',widget=forms.TextInput(attrs={'size':'40'}))
	solidity_version = forms.CharField(widget=forms.HiddenInput(),label='')
	solidity_version.widget.attrs.update({'value':'>=0.4.25 <0.6.0'})  
	id_carteira = forms.CharField(widget=forms.HiddenInput(),label='')
	tipo = forms.IntegerField(widget=forms.HiddenInput(),label='')
	tipo.widget.attrs.update({'value':'1'}) 

	class Meta:
		model = Contrato
		fields = ['id_carteira','name','id_cliente','solidity_version','tipo']

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user','')
		super(ContratoNovoForm, self).__init__(*args, **kwargs)
		clientes = Cliente.objects.filter(id_usuario=user)
		self.fields['id_cliente']=forms.ModelChoiceField(
			label='Cliente',
			queryset=clientes ,
			widget=forms.Select(attrs={'onchange':'javascript:vercli(this);'})
		)


class EditarContrato(forms.ModelForm):

	name = forms.CharField(label='Nome')
	wallet_address = forms.CharField(label='Carteira')
	wallet_address.widget.attrs.update({'size':'43'}) 
	solidity_version = forms.CharField(label='Versão Software')
	
	class Meta:
		model = Contrato
		fields = ['name','id_cliente','wallet_address','solidity_version']

class MostrarContrato(forms.ModelForm):

	name = forms.CharField(label='Nome',widget=forms.TextInput(attrs={'readonly':'True'}))
	wallet_address = forms.CharField(label='Carteira',widget=forms.TextInput(attrs={'readonly':'True'}))
	wallet_address.widget.attrs.update({'size':'43'}) 
	solidity_version = forms.CharField(label='Versão Software',widget=forms.TextInput(attrs={'readonly':'True'}))
	hash_address = forms.CharField(label='Numero do contrato',widget=forms.TextInput(attrs={'readonly':'True'}))
	hash_address.widget.attrs.update({'size':'57'}) 
	class Meta:
		model = Contrato
		fields = ['name','id_cliente','wallet_address','solidity_version','hash_address']

class PublicarContrato(forms.ModelForm):

	solidity_version = forms.CharField(widget=forms.HiddenInput(),label='')

	class Meta:
		model = Contrato	
		fields = ['name','id_cliente','solidity_version']

class DistribuirToken(forms.ModelForm):

	to_address = forms.CharField(
		label='Carteira',
		min_length = 42,
		widget=forms.TextInput(attrs={'size':'57'})
	)

	class Meta:
		model = ContratActions
		fields = ['to_address']

class PagamentoToken(forms.ModelForm):

	name = forms.CharField(label='Nome',widget=forms.TextInput(attrs={'size':'40'}))
	solidity_version = forms.CharField(widget=forms.HiddenInput(),label='')
	solidity_version.widget.attrs.update({'value':'>=0.4.25 <0.6.0'})  
	id_carteira = forms.CharField(widget=forms.HiddenInput(),label='')
	tipo = forms.IntegerField(widget=forms.HiddenInput(),label='')
	tipo.widget.attrs.update({'value':'4'}) 

	class Meta:
		model = Contrato
		fields = ['id_carteira','name','id_cliente','solidity_version','tipo']

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user','')
		super(PagamentoToken, self).__init__(*args, **kwargs)
		clientes = Cliente.objects.filter(id_usuario=user)
		self.fields['id_cliente']=forms.ModelChoiceField(
			label='Cliente',
			queryset=clientes ,
			widget=forms.Select(attrs={'onchange':'javascript:vercli(this);'})
		)
