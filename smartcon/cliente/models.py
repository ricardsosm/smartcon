from django.db import models
from usuario.models import Usuario

class Cliente(models.Model):
				
	name = models.CharField('Nome',max_length=20)	
	cpf = models.IntegerField(null=True, blank=True)
	tel = models.CharField('Telefone',max_length=20,null=True, blank=True)
	id_carteira= models.IntegerField(null=True, blank=True)
	create_at = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True
	)
	id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
