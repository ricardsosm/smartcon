import os 
from django.conf import settings

def Grava(form):

	nome = form.POST.get("name")
	nomearq = nome + ".sol"
	solidity_version = form.POST.get("solidity_version")
	id_cliente = form.POST.get("id_cliente")
	caminho = 'contract/'+id_cliente
	if not os.path.exists(caminho):
		os.mkdir(caminho)
	gra = caminho + '/' + nomearq 	
	#wallet_address = form.POST.get("wallet_address")
	arq = open(gra,"a")
	linha = 'pragma solidity ' + solidity_version + ';\n\n'
	main = 'contract contar {\n\n'
	carteira = '\taddress owner;\n'
	cliente = '\tuint cliente;\n'
	nome = '\tbytes32 name;\n\n'
	arq.write(linha)
	arq.write(main)
	arq.write('\tint private count = 0;\n')
	arq.write(carteira)
	arq.write(cliente)
	arq.write(nome)
	arq.write('\tfunction incrementCounter() public {\n\t\tcount += 1;\n\t}\n')
	arq.write('\tfunction decrementCounter() public {\n\t\tcount -= 1;\n\t}\n')
	arq.write('\tfunction getCount() public view returns (int) {\n\t\treturn count;\n\t}')
	main = '\n}'
	arq.write(main)

	arq.close()

def Apaga(con):

	caminho = 'contract/'+ str(con.id_cliente.id)
	arquivo = con.name + '.sol'
	apaga = caminho + arquivo
	dir = os.listdir(caminho)
	for file in dir:
		if file == arquivo:
			os.remove(caminho + '/'+ file)

def GravaAbi(con):

	caminho = 'contract/'+ str(con.id_cliente.id)
	if not os.path.exists(caminho):
		os.mkdir(caminho)
	nomearq = str(con.name) + "_abi.abi"
	grava = caminho + '/' + nomearq 

	arq = open(grava,"a")
	arq.write("abi = "+con.abi)
	arq.close()

