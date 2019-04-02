from django.db import models
from cliente.models import Cliente
from carteira.models import Carteira

class Contrato(models.Model):

	name = models.CharField(blank=True, max_length=20, null=True)
	hash_address = models.CharField(blank=True, max_length=100, null=True, unique=True)
	abi = models.TextField(null=True, max_length=2000)
	solidity_version  = models.CharField(blank=True, default='>=0.4.25 <0.6.0', max_length=20, null=True)
	ativo = models.BooleanField(null=True,blank=True)
	create_at = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True
	)
	id_carteira = models.IntegerField()
	id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,verbose_name="Cliente")

class ContratActions(models.Model):

	blocknumber = models.CharField(blank=True, max_length=30, null=True)
	status = models.BooleanField(null=True)
	contract_address = models.CharField(blank=True, max_length=100, null=True)
	from_adress	= models.CharField(blank=True, max_length=100, null=True)
	to_adress	= models.CharField(blank=True, max_length=100, null=True)
	transactionHash = models.CharField(blank=True, max_length=100, null=True)
	gasUsed = models.CharField(blank=True, max_length=30, null=True)
	create_at = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True
	)
	id_contrato = models.ForeignKey(Contrato,on_delete=models.CASCADE)

class ContratToken(models.Model):

	token = models.CharField(blank=True, max_length=15, null=True)
	simbolo = models.CharField(blank=True, max_length=5, null=True)
	contract_address = models.CharField(blank=True, max_length=100, null=True)
	quantidade = models.CharField(blank=True, max_length=5, null=True)
	digitos = models.CharField(blank=True, max_length=5, null=True)
	create_at = models.DateTimeField(
		'Criando em',auto_now_add=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True
	)
	id_contrato = models.ForeignKey(Contrato,on_delete=models.CASCADE)