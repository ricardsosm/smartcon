from django.db import models
from cliente.models import Cliente

class Carteira(models.Model):
				
	name = models.CharField('Nome',max_length=20,null=True, blank=True)	
	saldo = models.FloatField(null=True, blank=True)
	private_key = models.CharField('Chave Privada',max_length=200,null=True, blank=True)
	public_key = models.CharField('Chave Privada',max_length=200,null=True, blank=True)
	create_at = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True
	)
	id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)


