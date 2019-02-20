import sys, time , pprint
from web3 import Web3, HTTPProvider
from solc import compile_source
from eth_account import Account

w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/5b15a8a0ea6f4ba28356608cbac65c35')) 
_key = '77843608035084c2deb8e8ec5f0d4f1887cefafebdb32da361cc36d54742d419'
_address = '0x928783707f0a4ed28D3e9C78eC68BBF2378bDFc8'

nonce = w3.eth.getTransactionCount(_address)

gas = w3.eth.gasPrice
gas_limit = w3.eth.getBlock("latest").gasLimit


def compile_source_file(file_path):
  print(file_path)
  with open(file_path, 'r') as f:
    source = f.read()
    print(f)
  return compile_source(source)

def deploy_contract(w3, contract_interface):
  tx_hash = w3.eth.contract(
    abi=contract_interface['abi'],
    bytecode=contract_interface['bin']
  ).deploy(transaction)
  address = w3.eth.getTransactionReceipt(tx_hash)['contractAddress']
  return address


def wait_for_receipt(w3, tx_hash, poll_interval):
  while True:
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    if tx_receipt:
      return tx_receipt
    time.sleep(poll_interval)

contract_source_path = 'contrato.sol'
compiled_sol = compile_source_file('contrato.sol')

contract_id, contract_interface = compiled_sol.popitem()

contract_ = w3.eth.contract(
    abi=contract_interface['abi'],
    bytecode=contract_interface['bin'])

acct = Account.privateKeyToAccount('77843608035084c2deb8e8ec5f0d4f1887cefafebdb32da361cc36d54742d419');

construct_txn = contract_.constructor().buildTransaction({
    'from': acct.address,
    'nonce': w3.eth.getTransactionCount(acct.address),
    'gas': 1728712,
    'gasPrice': w3.toWei('21', 'gwei')})

signed = acct.signTransaction(construct_txn)

w3.eth.sendRawTransaction(signed.rawTransaction)

