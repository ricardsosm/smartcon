from django import forms
from django.forms.models import modelformset_factory
from sistema.mail import send_mail_template
from .models import Contrato
from cliente.models  import Cliente
from django.forms import modelformset_factory
from django.contrib.auth import get_user_model

User = get_user_model()

class ContratoNovoForm(forms.ModelForm):

	name = forms.CharField(label='Nome')
	wallet_address = forms.CharField(label='Carteira',widget=forms.TextInput(attrs={'placeholder':'Numero da carteira'}))
	wallet_address.widget.attrs.update({'size':'35'}) 
	solidity_version = forms.CharField(widget=forms.HiddenInput(),label='')
	solidity_version.widget.attrs.update({'value':'0.4.21'})  

	class Meta:
		model = Contrato
		fields = ['name','id_cliente','wallet_address','solidity_version']

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user','')
		super(ContratoNovoForm, self).__init__(*args, **kwargs)
		self.fields['id_cliente']=forms.ModelChoiceField(label='Cliente',queryset=Cliente.objects.filter(id_usuario=user))

class EditarContrato(forms.ModelForm):

	name = forms.CharField(label='Nome')
	wallet_address = forms.CharField(label='Carteira')
	solidity_version = forms.CharField(label='Versão Software')
	
	class Meta:
		model = Contrato
		fields = ['name','id_cliente','wallet_address','solidity_version']


