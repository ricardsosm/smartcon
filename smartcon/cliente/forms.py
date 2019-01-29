from django import forms
from sistema.mail import send_mail_template
from .models  import Cliente
from usuario.models import Usuario

class ClienteNovoForm(forms.ModelForm):

	name = forms.CharField(label='Nome',widget=forms.TextInput(attrs={'placeholder':'Digite seu Nome'}))
	cpf = forms.CharField(label='CPF',widget=forms.TextInput(attrs={'placeholder':'Digite seu CPF'}))
	tel = forms.CharField(label='Telefone',widget=forms.TextInput(attrs={'placeholder':'Digite seu Telefone','class':'tel'})) 
	id_carteira = forms.CharField(label='Carteira',widget=forms.TextInput(attrs={'class':'carteira'})) 
	id_usuario = forms.ModelChoiceField (
		queryset=Usuario.objects.all(),
		widget=forms.HiddenInput(),
		label='',
		)

	class Meta:
		model = Cliente
		fields = ['name','cpf','tel','id_carteira','id_usuario']

class EditarCliente(forms.ModelForm):

	name = forms.CharField(label='Nome')
	cpf = forms.CharField(label='CPF',widget=forms.TextInput(attrs={'class':'cpf'}))
	tel = forms.CharField(label='Telefone',widget=forms.TextInput(attrs={'class':'tel'})) 
	id_carteira = forms.CharField(label='Carteira',widget=forms.TextInput(attrs={'class':'carteira'}))

	class Meta:
		model = Cliente
		fields = ['name','cpf','tel','id_carteira']

class MostrarCliente(forms.ModelForm):

	name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
	cpf = forms.CharField(label='CPF',widget=forms.TextInput(attrs={'class':'cpf','readonly':'True'}))
	tel = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
	id_carteira = forms.IntegerField(label='Carteira',widget=forms.TextInput(attrs={'class':'carteira','readonly':'True'}))

	class Meta:
		model = Cliente
		fields = ['name','cpf','tel','id_carteira']
