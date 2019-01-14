from django.db import models

class Usuario(models.Model):

	name = models.CharField('Nome',max_length=20)
	slug = models.SlugField('Atalho')	
	password = models.CharField('Senha',max_length=100)
	salt = models.CharField('Salt',max_length=10)
	level = models.CharField('Nivel',max_length=100)
	access = models.IntegerField(null=True, blank=True)
	ip_last = models.GenericIPAddressField(null=True, blank=True)

	start_date = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True
	)
