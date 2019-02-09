import time 
from web3 import Web3, HTTPProvider 
import contract_abi

contract_address = '0x8b62d2F546cbFfF6B2B42d664fD87B5c6E9e18F9' 
wallet_private_key = '77843608035084c2deb8e8ec5f0d4f1887cefafebdb32da361cc36d54742d419'
wallet_address = '0x928783707f0a4ed28D3e9C78eC68BBF2378bDFc8'

w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/5b15a8a0ea6f4ba28356608cbac65c35')) 
w3.eth.enable_unaudited_features ()
contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi)


def send_ether_to_contract(amount_in_ether):

    amount_in_wei = w3.toWei(amount_in_ether,'ether');
    nonce = w3.eth.getTransactionCount(wallet_address)
    contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi)

    txn_dict = {
            'to': contract_address,
            'value': amount_in_wei,
            'gas': 2000000,
            'gasPrice': w3.toWei('40', 'gwei'),
            'nonce': nonce,
            'chainId': 3
    }

    signed_txn = w3.eth.account.signTransaction(txn_dict, wallet_private_key)

    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    txn_receipt = None
    count = 0
    while txn_receipt is None and (count < 30):

        txn_receipt = w3.eth.getTransactionReceipt(txn_hash)

        print(txn_receipt)

        time.sleep(10)


    if txn_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    return {'status': 'added', 'txn_receipt': txn_receipt}

    txn_receipt = None
    count = 0
    while txn_receipt is None and (count < 30):

        txn_receipt = w3.eth.getTransactionReceipt(txn_hash)

        print(txn_receipt)

        time.sleep(10)

def check_whether_address_is_approved(address):
	return contract.functions.isApproved(address).call()

def broadcast_an_opinion(covfefe):


    nonce = w3.eth.getTransactionCount(wallet_address)

    txn_dict = contract.functions.broadcastOpinion(covfefe).buildTransaction({
        'chainId': 3,
        'gas': 140000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = w3.eth.account.signTransaction(txn_dict, private_key=wallet_private_key)

    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    tx_receipt = w3.eth.getTransactionReceipt(result)

    count = 0
    while tx_receipt is None and (count < 30):

        time.sleep(10)

        tx_receipt = w3.eth.getTransactionReceipt(result)

        print(tx_receipt)


    if tx_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    processed_receipt = contract.events.OpinionBroadcast().processReceipt(tx_receipt)

    print(processed_receipt)
    
    output = "Address {} broadcasted the opinion: {}"\
        .format(processed_receipt[0].args._soapboxer, processed_receipt[0].args._opinion)
    print(output)

    return {'status': 'added', 'processed_receipt': processed_receipt}

if __name__ == "__main__":

    send_ether_to_contract(0.03)

    is_approved = check_whether_address_is_approved(wallet_address)
    
    print(is_approved)

    broadcast_an_opinion('Despite the Smart Constant ')