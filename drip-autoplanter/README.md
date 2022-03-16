# The Garden
The [Garden](https://theanimalfarm/referrals/0xeDb0951cF765b6E19881497C407C39914D78c597) is a game where players
deposit drip-busd to purchase plants. Plants make seeds at a rate of 86,400 per day and when you accumulate
enough seeds (2,592,000) you reach the minimum threshold to either compount or claim. 

This bot is only configured to plant, not harvest. It can be configured to plant after a certain # of
plants have been earned, so it can be used by someone making 1 plant a day to 100+ plants a day. The seed loss 
per plant is equivilent to the number of plants you have

## Setup Autoplanter

This code was specifically written to be as secure as possible, since signing transactions requires the use of
a wallet's private key. It's imparative you use the encryption outlined in the code to best protect yourself
in the event your computer is ever compomised. 

1. Download [Python](https://www.python.org/downloads/) if you do not already have it. I was not able to get this code
to work on Python 3.9, so I would recommending using Python 3.7 or 3.8. There are a number of resources that will walk 
you through installing Python depending on your operating system.

2. Once Python is installed, install the required python packages. Open a terminal and run Python. Then, run the command shown below. 
 
```bash
$ python -m pip install -r requirements.txt
```

3. In a python terminal, import `cryptography` and encrypt your private key

```py
>>>from cryptography.fernet import Fernet
>>>key = Fernet.generate_key()
>>>key.decode()
```

4. Open `.env.example` and replace the key with the key you generated in step 3. Save the file without .example at the end. This key 
SHOULD contain the quotes before and after the key.

5. Encrypt your private key. 

```py
>>>fernet = Fernet(key)
>>>encMessage = fernet.encrypt('YOURKEYHERE'.encode())
>>>encMessage.decode()
```

If you are using MetaMask, your private key can be found under account details -> Export Private Key. If you are using TrustWallet, you need to take your seed
phrase and import your wallet into MetaMask. Then you can export the private key. Using your seed phrase for TrustWallet will not work. 

6. Take the value in `encMessage.decode()`, create a file called `key.txt` and save the text in the file. This file SHOULD NOT contain quotes. 

## Using the Autoplanter

```bash
$ python garden.py --help
usage: garden.py [-h] -p PLANTS_TO_COMPOUND -w WALLET_ADDRESS

Drip Autoplanter

optional arguments:
  -h, --help            show this help message and exit
  -p PLANTS_TO_COMPOUND, --plants-to-compound PLANTS_TO_COMPOUND
                        Number of plants to compound at a time
  -w WALLET_ADDRESS, --wallet-address WALLET_ADDRESS
                        Your wallet address
```

In a terminal window, navigate to the location where you saved all the files. Run the `garden.py` file with the required arguments.

```bash
$ python garden.py -p 1 -w <your-wallet-address>
```

This terminal window will always need to remain open for the autoplanter to function. If the terminal window closes, just execute
the command again.

If this autoplanter helps you, consider supporting me by sending me an airdrop. 

**wallet:** *0xeDb0951cF765b6E19881497C407C39914D78c597*

If you haven't already invested in the [Animal Farm](https://theanimalfarm/referrals/0xeDb0951cF765b6E19881497C407C39914D78c597), then I highly recommend you doing so!