import sys, time , pprint
from web3 import Web3, HTTPProvider
from solc import compile_source
from eth_account import Account

class Fabrica:

  def compile_source_file(self,file_path):
    with open(file_path, 'r') as f:
      source = f.read()
      ret = compile_source(source)
    return ret

  def __init__(self,file_path,key):

    self.w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/5b15a8a0ea6f4ba28356608cbac65c35')) 
 
    compiled_sol = self.compile_source_file(file_path)
    contract_id, contract_interface = compiled_sol.popitem()
    self.myabi=contract_interface['abi']
    contract_ = self.w3.eth.contract(
      abi=contract_interface['abi'],
      bytecode=contract_interface['bin']
    )

    acct = Account.privateKeyToAccount(key);

    construct_txn = contract_.constructor().buildTransaction({
      'from': acct.address,
      'nonce': self.w3.eth.getTransactionCount(acct.address),
      'gas': 1728712,
      'gasPrice': self.w3.toWei('21', 'gwei')}
    )
    self.signed = acct.signTransaction(construct_txn)

  def enviar(self):
    self.address = w3.eth.sendRawTransaction(self.signed.rawTransaction)
    return self.address

'''
# com assinatura interna
key =  conta.privateKey
nonce = w3.eth.getTransactionCount(conta.address)
gas = w3.eth.gasPrice
gas_limit = w3.eth.getBlock("latest").gasLimit

transaction = {
  'to': '0x928783707f0a4ed28D3e9C78eC68BBF2378bDFc8',
  'value': 1000000000,
  'gas': 2000000,
  'gasPrice': gas_limit,
  'nonce': nonce, 
  'chainId': 3
}

signed = w3.eth.account.signTransaction(transaction, key)
signed.rawTransaction
signed.hash
signed.r
signed.s
signed.v
w3.eth.sendRawTransaction(w3.toHex(signed.rawTransaction))

0x2372d3cea057d871a6d487c7e00cd11ef8cf3ec5c16c7986881d8a854fd4818b
'''
