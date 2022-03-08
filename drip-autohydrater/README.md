# Drip Intro

[Drip](https://drip.community) is a deflationary daily ROI platform that allows
you to earn 1% daily return on your investment sustainably through a tax system
on transactions. It also allows team building through a referral system, and most
importantly, compound interest. 


## The Faucet

The [Faucet](https://drip.community/faucet) is a low-risk, high reward contract that operates similar to a high yield 
certificate of deposit. You can participate by purchasing drip from the [swap page](https://drip.community/fountain).

It is necessary, depending on your deposit size, to compound up to several times a day. The purpose of this code
is to do this automatically for you so you don't have to. 

## Setup Autohydrater

This code was specifically written to be as secure as possible, since signing transactions requires the use of
a wallet's private key. It's imparative you use the encryption outlined in the code to best protect yourself
in the event your computer is ever compomised. 

1. Download [Python](https://www.python.org/downloads/) if you do not already have it. I was not able to get this code
to work on Python 3.9, so I would recommending using Python 3.7 or 3.8. There are a number of resources that will walk 
you through installing Python depending on your operating system.

2. Once Python is installed, the following packages need to be installed. Open a terminal and run Python. Then, run the commands shown below. 

web3, cryptography, python-dotenv
 
```bash
$ python -m pip install web3
$ python -m pip install cryptography
$ python -m pip install python-dotenv
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

7. Open the `hydrate.py` file and replace the string stored in `wallet_public_addr` with your own public wallet.

## Using the Autohydrater

In a terminal window, navigate to the location where you saved all the files. Run the `hydrate.py` file.

```bash
$ python hydrate.py
```

This terminal window will always need to remain open for the autohydrater to function. If the terminal window closes, just execute
`hydrate.py` again.

If this autohydrater helps you, consider supporting me by sending me an airdrop. 

**wallet:** *0xeDb0951cF765b6E19881497C407C39914D78c597*

If you haven't already invested in the [Animal Farm](https://theanimalfarm/referrals/0xeDb0951cF765b6E19881497C407C39914D78c597), then I highly recommend you doing so!