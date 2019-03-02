from django.db import models
from usuario.models import Usuario

class Cliente(models.Model):
				
	name = models.CharField('Nome',max_length=30)	
	cpf = models.CharField(null=True, blank=True, unique=True,max_length=14)
	tel = models.CharField('Telefone',max_length=20,null=True, blank=True)
	id_carteira= models.CharField(null=True, blank=True,max_length=100, unique=True)
	saldo_carteira = models.FloatField(null=True, blank=True)
	create_at = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True
	)
	id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

	def set(self,pk):
		self.id_usuario = pk
		return  True

	def __str__(self):
		return self.name