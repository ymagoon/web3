import os
from web3 import Web3
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# load environment variables
load_dotenv()

rpc_url = "https://bsc-dataseed.binance.org:443"
web3 = Web3(Web3.HTTPProvider(rpc_url))

def connect_to_contract(contract_addr, contract_abi):
    contract = web3.eth.contract(address=contract_addr, abi=contract_abi)
    return contract


def send_txn(txn, private_key_encrypt):
    # get key from environment variable
    fernet_key = os.environ['FERNET_KEY']
    
    # decode encrypted key
    private_key = Fernet(fernet_key.encode()).decrypt(private_key_encrypt.encode()).decode()
    
    txn_signed = web3.eth.account.signTransaction(txn, private_key)
    tx_hash = web3.eth.sendRawTransaction(txn_signed.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    return tx_receipt


def get_tx_options(public_address, gas=500000):
    return {
        "nonce": web3.eth.getTransactionCount(public_address),
        "from": public_address,
        "gas": gas,
        "gasPrice": web3.toWei(5, "gwei")
    }
