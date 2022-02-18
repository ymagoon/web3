import time
import wallet

PrivateKey_FilePath = "key.txt"
Wallet_PublicAddress = "0xeDb0951cF765b6E19881497C407C39914D78c597"
KEY_Wallet = open(PrivateKey_FilePath, "r").readline()

faucet_contract = wallet.connect_to_contract(wallet.faucet)

def deposit_amount(addr):
    user_totals = faucet_contract.functions.userInfoTotals(addr).call()
    return user_totals[1]/1000000000000000000

def available(addr):
    return faucet_contract.functions.claimsAvailable(addr).call() / 1000000000000000000

def hydrate():
    txn = faucet_contract.functions.roll().buildTransaction(wallet.getTxOptions(Wallet_PublicAddress, 500000))
    return wallet.sendTxn(txn, KEY_Wallet)

while True:
    deposit = deposit_amount(Wallet_PublicAddress)
    hydrate_amount = deposit * .01
    avail = available(Wallet_PublicAddress)
    
    if avail >= hydrate_amount:
        hydrate()
        print(f"Hydrated! {avail} added to deposit")
        time.sleep(60)
    else:
        print(f"Hydrate not ready only {avail:.2f} Drip available")
        for second in range(0, 60*60, 60):
                print(f"Sleep time remaining: {(60*60 - second)/60} min",end="\r")
                time.sleep(60)
