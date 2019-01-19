from django import forms
from sistema.mail import send_mail_template
from .models  import Cliente
from usuario.models import Usuario

class ClienteNovoForm(forms.ModelForm):

	name = forms.CharField(label='Nome')
	cpf = forms.IntegerField(label='CPF')
	tel = forms.IntegerField(label='Telefone') 
	id_carteira = forms.IntegerField(label='Carteira') 
	id_usuario = forms.ModelChoiceField (
		queryset=Usuario.objects.all(),
		widget=forms.HiddenInput()
		)

	class Meta:
		model = Cliente
		fields = ['name','cpf','tel','id_carteira','id_usuario']
