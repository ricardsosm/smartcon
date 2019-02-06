from django.db import models
from cliente.models import Cliente

class Carteira(models.Model):
				
	name = models.CharField('Nome',max_length=20)	
	saldo_carteira = models.FloatField(null=True, blank=True)
	create_at = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True
	)
	id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)

	def set(self,pk):
		self.cliente = pk
		return  True

	def __str__(self):
		return self.name
