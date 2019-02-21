from django.db import models
from cliente.models import Cliente

class Contrato(models.Model):

	name = models.CharField(blank=True, max_length=20, null=True)
	contract_address = models.CharField(blank=True, max_length=100, null=True, unique=True)
	abi = models.TextField(null=True, max_length=2000)
	wallet_private_key = models.CharField(blank=True, max_length=100, null=True, unique=True)
	wallet_address = models.CharField(blank=True, max_length=100, null=True, unique=True)
	solidity_version  = models.CharField(blank=True, default='>=0.4.21 <0.6.0', max_length=20, null=True)
	ativo = models.BooleanField(default=False)
	create_at = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True
	)
	id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,verbose_name="Cliente")

class ContratActions(models.Model):

	number = models.CharField(blank=True, max_length=100, null=True, unique=True)
	create_at = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True
	)
	id_contrato = models.ForeignKey(Contrato,on_delete=models.CASCADE)
