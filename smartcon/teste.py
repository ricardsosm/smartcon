import sys, time , pprint
from web3 import Web3, HTTPProvider
from solc import compile_source
from eth_account import Account
from contrato.models import Contrato, ContratActions
from carteira.models import Carteira

import contract_abi

w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/5b15a8a0ea6f4ba28356608cbac65c35')) 
w3.eth.enable_unaudited_features ()
abi = con.abi

ca = Carteira.objects.get(pk='2')
_key = ca.private_key
_address = ca.public_key

con = Contrato.objects.get(pk='4')
cona = ContratActions.objects.get(id_contrato = con.pk)
conadress = cona.contract_address


myContract = w3.eth.contract(address=conadress, abi=con.abi)

print(myContract)

one = myContract.functions.getCount().call()

