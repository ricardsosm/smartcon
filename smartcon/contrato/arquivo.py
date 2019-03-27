import os 
from django.conf import settings

def Token(form):

	nome = form.POST.get("name")
	carteira = form.POST.get("wallet_address")
	nomearq = nome + ".sol"
	solidity_version = form.POST.get("solidity_version")
	id_cliente = form.POST.get("id_cliente")
	token = form.POST.get("token")
	simbolo = form.POST.get("simbolo")
	dig = form.POST.get("digitos")
	qtde = form.POST.get("qtde")
	valor = (int(dig) * int(qtde))
	qtde = str(valor)
	caminho = 'contract/'+id_cliente
	if not os.path.exists(caminho):
		os.mkdir(caminho)
	gra = caminho + '/' + nomearq 	
	#wallet_address = form.POST.get("wallet_address")
	arq = open(gra,"w")
	linha = 'pragma solidity ' + solidity_version + ';\n\n'
	ini = 'contract ERC20Interface {\n\tfunction totalSupply() public constant returns (uint);\n\tfunction balanceOf(address tokenOwner) public constant returns (uint balance);\n\tfunction allowance(address tokenOwner, address spender) public constant returns (uint remaining);\n\tfunction transfer(address to, uint tokens) public returns (bool success);\n\tfunction approve(address spender, uint tokens) public returns (bool success);\n\tfunction transferFrom(address from, address to, uint tokens) public returns (bool success);\n\tevent Transfer(address indexed from, address indexed to, uint tokens);\n\tevent Approval(address indexed tokenOwner, address indexed spender, uint tokens);\n}\n\n'
	ini2 = 'contract ApproveAndCallFallBack {\n\tfunction receiveApproval(address from, uint256 tokens, address token, bytes data) public;\n}\n\n'
	ini3 = 'contract Owned {\n\taddress public owner;\n\taddress public newOwner;\n\n\tevent OwnershipTransferred(address indexed _from, address indexed _to);\n\n\tconstructor() public {\n\t\towner = msg.sender;\n\t}\n\n\tmodifier onlyOwner {\n\t\trequire(msg.sender == owner);\n\t\t_;\n\t}\n\n\tfunction transferOwnership(address _newOwner) public onlyOwner {\n\t\tnewOwner = _newOwner;\n\t}\n\n\tfunction acceptOwnership() public {\n\t\trequire(msg.sender == newOwner);\n\t\temit OwnershipTransferred(owner, newOwner);\n\t\towner = newOwner;\n\t\tnewOwner = address(0);\n\t}\n}\n\n'
	main = 'contract ' + token + ' is ERC20Interface, Owned {\n\n'
	arq.write(linha)
	arq.write(ini)
	arq.write(ini2)
	arq.write(ini3)
	arq.write(main)
	arq.write('\tstring public symbol;\n\tstring public  name;\n\tuint8 public decimals;\n\tuint public _totalSupply;\n')
	arq.write('\tmapping(address => uint) balances;\n\tmapping(address => mapping(address => uint)) allowed;\n\n')
	arq.write('\tconstructor() public {\n\t\tsymbol = "'+simbolo+'";\n\t\tname = "'+token+'";\n\t\tdecimals = '+dig+';\n\t\t_totalSupply = '+qtde+';\n\t\tbalances['+carteira+'] = _totalSupply;\n\t\temit Transfer(address(0), '+carteira+', _totalSupply);\n\t}\n\n')
	arq.write('\tfunction safeAdd(uint a, uint b) public pure returns (uint c) {\n\t\tc = a + b;\n\t\trequire(c >= a);\n\t}\n')
	arq.write('\tfunction safeSub(uint a, uint b) public pure returns (uint c) {\n\t\trequire(b <= a);\n\t\tc = a - b;\n\t}\n')
	arq.write('\tfunction safeMul(uint a, uint b) public pure returns (uint c) {\n\t\tc = a * b;\n\t\trequire(a == 0 || c / a == b);\n\t}\n')
	arq.write('\tfunction safeDiv(uint a, uint b) public pure returns (uint c) {\n\t\trequire(b > 0);\n\t\tc = a / b;\n\t}\n\n')
	arq.write('\tfunction totalSupply() public constant returns (uint) {\n\t\treturn _totalSupply  - balances[address(0)];\n\t}\n\n')
	arq.write('\tfunction balanceOf(address tokenOwner) public constant returns (uint balance) {\n\t\treturn balances[tokenOwner];\n\t}\n\n')
	arq.write('\tfunction transfer(address to, uint tokens) public returns (bool success) {\n\t\tbalances[msg.sender] = safeSub(balances[msg.sender], tokens);\n\t\tbalances[to] = safeAdd(balances[to], tokens);\n\t\temit Transfer(msg.sender, to, tokens);\n\t\treturn true;\n\t}\n\n')
	arq.write('\tfunction approve(address spender, uint tokens) public returns (bool success) {\n\t\tallowed[msg.sender][spender] = tokens;\n\t\temit Approval(msg.sender, spender, tokens);\n\t\treturn true;\n\t}\n\n')
	arq.write('\tfunction transferFrom(address from, address to, uint tokens) public returns (bool success) {\n\t\tbalances[from] = safeSub(balances[from], tokens);\n\t\tallowed[from][msg.sender] = safeSub(allowed[from][msg.sender], tokens);\n\t\tbalances[to] = safeAdd(balances[to], tokens);\n\t\temit Transfer(from, to, tokens);\n\t\treturn true;\n\t}\n\n')
	arq.write('\tfunction allowance(address tokenOwner, address spender) public constant returns (uint remaining) {\n\t\treturn allowed[tokenOwner][spender];\n\t}\n\n')
	arq.write('\tfunction approveAndCall(address spender, uint tokens, bytes data) public returns (bool success) {\n\t\tallowed[msg.sender][spender] = tokens;\n\t\temit Approval(msg.sender, spender, tokens);\n\t\tApproveAndCallFallBack(spender).receiveApproval(msg.sender, tokens, this, data);\n\t\treturn true;\n\t}\n\n')
	arq.write('\tfunction () public payable {\n\t\trevert();\n\t}\n\n')
	arq.write('\tfunction transferAnyERC20Token(address tokenAddress, uint tokens) public onlyOwner returns (bool success) {\n\t\treturn ERC20Interface(tokenAddress).transfer(owner, tokens);\n\t}\n')
	arq.write('\n}')
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

	arq = open(grava,"w")
	arq.write("abi = "+str(con.abi))
	arq.close()

