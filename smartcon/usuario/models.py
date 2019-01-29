from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,UserManager
from django.conf import settings

class Usuario(AbstractBaseUser,PermissionsMixin):

	username = models.CharField('Nome do Usuario', max_length=30,unique=True,default='')
	name = models.CharField('Nome',max_length=50,blank = True)
	email = models.EmailField('Email',default='')
	is_active = models.BooleanField('Esta ativo',blank=True,default=True)
	is_staff = models.BooleanField('Master',blank=True,default=False)
	access = models.IntegerField(null=True, blank=True)
	ip_last = models.GenericIPAddressField(null=True, blank=True)
	date_joined = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True
	)

	objects = UserManager()

	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS =  ['email']

	def __str__(self):
		return self.name or self.username

	def get_short_name(self):
		return self.username

	def get_full_name(self):
		return str(self)

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'
		ordering = ['name']

		
class PasswordReset(models.Model):

	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, verbose_name='Usuario',
		on_delete=models.CASCADE,
		related_name='resets'
	)

	key = models.CharField('Chave', max_length=100, unique=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	confirmed = models.BooleanField('Confirmado', blank=True,default=False)

	def __str__(self):
		return '{0} em {1}'.format(self.user,self.created_at)

	class Meta:
		verbose_name = 'Nova Senha'
		verbose_name_plural = 'Novas Senhas'
		ordering = ['-created_at']
