

def Grava(form):

	nome = form.POST.get("name")
	solidity_version = form.POST.get("solidity_version")
	id_cliente = form.POST.get("id_cliente")
	wallet_address = form.POST.get("wallet_address")
	arq = open("contrato.sol","w")
	linha = 'pragma solidity ' + solidity_version + ';\n\n'
	main = 'contract contar {\n\n'
	carteira = '\taddress owner '+wallet_address+';\n'
	cliente = '\tuint cliente = '+ id_cliente + ';\n'
	nome = '\tbytes32 name "'+ nome +'";\n\n'
	arq.write(linha)
	arq.write(main)
	arq.write('\tint private count = 0;\n')
	arq.write(carteira)
	arq.write(cliente)
	arq.write(nome)
	arq.write('\tfunction incrementCounter() public {\n\t\tcount += 1;\n\t}\n')
	arq.write('\tfunction decrementCounter() public {\n\t\tcount -= 1;\n\t}\n')
	arq.write('\tfunction getCount() public constant returns (int) {\n\t\treturn count;\n\t}')
	main = '\n}'
	arq.write(main)

	arq.close