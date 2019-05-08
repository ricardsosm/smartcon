from django.db import models
from cliente.models import Cliente

class Carteira(models.Model):
				
	name = models.CharField('Nome',max_length=20,null=True, blank=True)	
	saldo = models.FloatField(null=True, blank=True)
	private_key = models.CharField('Chave Privada',max_length=250,null=True, blank=True)
	public_key = models.CharField('Chave Privada',max_length=200,null=True, blank=True)
	create_at = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True
	)
	id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class CarteiraToken(models.Model):

	id_token = models.IntegerField(null=True, blank=True)
	token = models.CharField(blank=True, max_length=15, null=True)
	simbolo = models.CharField(blank=True, max_length=5, null=True)
	digitos = models.CharField(blank=True, max_length=5, null=True)
	saldo = models.FloatField(null=True, blank=True)
	contract = models.CharField(blank=True, max_length=75, null=True)
	id_carteira = models.ForeignKey(Carteira,on_delete=models.CASCADE)