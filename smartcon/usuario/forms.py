from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from sistema.mail import send_mail_template
from sistema.utils import generate_hash_key
from usuario.models import PasswordReset

User = get_user_model()

class PasswordResetForm(forms.Form):

	email = forms.EmailField(label='E-mail')

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			return email
		raise forms.ValidationError('Nenhum usuário encontrado com este e-mail')

	def save(self):
		user = User.objects.get(email=self.cleaned_data['email'])
		key = generate_hash_key(user.email)
		reset = PasswordReset(key=key,user=user)
		reset.save()
		template_name = 'password_reset_mail.html'
		subject = 'Criar nova senha'
		context = {
			'reset': reset,
		}
		send_mail_template(subject,template_name,context,[user.email])

class EditarConta(forms.ModelForm):
	
	def clean_email(self):
		email= self.cleaned_data['email']
		queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
		if queryset.exists():
			raise forms.ValidationError('Email já existe')
		return email

	class Meta:
		model = User
		fields = ['username','name','email']

class ApagarConta(forms.ModelForm):

	class Meta:
		model = User
		fields = ['id']
