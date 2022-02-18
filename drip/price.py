import json
import requests
from web3 import Web3

f = open('faucet_abi.json')
faucet_abi = json.load(f)

def deposit_amount(addr):
    bsc = "https://bsc-dataseed.binance.org/"
    web3 = Web3(Web3.HTTPProvider(bsc))
    drip_contract_addr = "0xFFE811714ab35360b67eE195acE7C10D93f89D8C"
    faucet_contract = web3.eth.contract(address=drip_contract_addr, abi=faucet_abi)
    user_totals = faucet_contract.functions.userInfoTotals(addr).call()
    return user_totals[1]/1000000000000000000

def get_drip_price():
    drip_pcs = requests.get("https://api.drip.community/prices/")
    drip_price = drip_pcs.json()[-1]['value']
    return drip_price

# wallets = ['0xeDb0951cF765b6E19881497C407C39914D78c597']

# total_drip, total_value = 0, 0
# for wallet in wallets:
#    deposit = deposit_amount(wallet)
#    deposit_value = deposit * drip_price
#    total_drip += deposit
#    total_value += deposit_value
#    
#    print(f"{wallet[-4:]}========================")
#    print(f"{deposit=:.2f}")
#    print(f"{deposit_value=:.2f}")
#    print("============================")

# print(f"{total_drip=:.2f}")
# print(f"{total_value=:.2f}")
