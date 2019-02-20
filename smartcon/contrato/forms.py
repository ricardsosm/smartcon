from django import forms
from django.forms.models import modelformset_factory
from sistema.mail import send_mail_template
from .models import Contrato
from cliente.models  import Cliente
from django.forms import modelformset_factory
from django.contrib.auth import get_user_model

User = get_user_model()

class ContratoNovoForm(forms.ModelForm):

	name = forms.CharField(label='Nome',widget=forms.TextInput(attrs={'size':'40'}))
	wallet_address = forms.CharField(
		label='Carteira',
		widget=forms.TextInput(attrs={'placeholder':'Numero da carteira'})
	)
	wallet_address.widget.attrs.update({'size':'42'}) 
	solidity_version = forms.CharField(widget=forms.HiddenInput(),label='')
	solidity_version.widget.attrs.update({'value':'>=0.4.21 <0.6.0'})  

	class Meta:
		model = Contrato
		fields = ['name','id_cliente','wallet_address','solidity_version']

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user','')
		super(ContratoNovoForm, self).__init__(*args, **kwargs)
		self.fields['id_cliente']=forms.ModelChoiceField(
			label='Cliente',
			queryset=Cliente.objects.filter(id_usuario=user),
			widget=forms.Select(attrs={'onchange':'javascript:vercli(this);'})
		)

class EditarContrato(forms.ModelForm):

	name = forms.CharField(label='Nome')
	wallet_address = forms.CharField(label='Carteira')
	wallet_address.widget.attrs.update({'size':'42'}) 
	solidity_version = forms.CharField(label='Versão Software')
	
	class Meta:
		model = Contrato
		fields = ['name','id_cliente','wallet_address','solidity_version']

class MostrarContrato(forms.ModelForm):

	name = forms.CharField(label='Nome',widget=forms.TextInput(attrs={'readonly':'True'}))
	wallet_address = forms.CharField(label='Carteira',widget=forms.TextInput(attrs={'readonly':'True'}))
	wallet_address.widget.attrs.update({'size':'42'}) 
	solidity_version = forms.CharField(label='Versão Software',widget=forms.TextInput(attrs={'readonly':'True'}))
	
	class Meta:
		model = Contrato
		fields = ['name','id_cliente','wallet_address','solidity_version']
