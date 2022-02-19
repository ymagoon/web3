# Drip Intro

[Drip][drip.community/faucet] is a deflationary daily ROI platform that allows
you to earn 1% daily return on your investment sustainably through a tax system
on transactions. It also allows team building through a referral system, and most
importantly, compound interest. 


## The Faucet

The [Faucet](drip.community/faucet) is a low-risk, high reward contract that operates similar to a high yield 
certificate of deposit. You can participate by purchasing drip from the [swap page](drip.community/fountain).

It is necessary, depending on your deposit size, to compound up to several times a day. The purpose of this code
is to do this automatically for you so you don't have to. 

## Setup Autohydrater

This code was specifically written to be as secure as possible, since signing transactions requires the use of
a wallet's private key. It's imparative you follow use the encryption outlined in the code to best protect yourself
in the event your computer is ever compomised. 

1. Download [Python](https://www.python.org/downloads/) if you do not already have it. I was not able to get this code
to work on Python 3.9, so I would recommending using Python 3.7 or 3.8. There are a number of resources that will walk 
you through installing Python depending on your operating system.

2. Once Python is installed, the following packages need to be installed.

web3, cryptography, python-dotenv
 
```bash
$ python -m pip install web3
$ python -m pip install cryptography
$ python -m pip install python-dotenv
```

3. In a python terminal, import `cryptography` and encrypt your private key

```bash
>>>import cryptography
>>>key = Fernet.generate_key()
>>>fernet = Fernet(key.encode())
>>>encMessage = fernet.encrypt('YOURKEYHERE'.encode())
>>>encMessage.decode()
```

4. Take the value in `encMessage`, create a file called `key.txt` and save the text in the file 

5. Open the .env.example file and replace the key with the key you generated in step 3. Save the file without .example at the end. 

6. Open the `hydrate.py` file and replace the string stored in `wallet_public_addr` with your own public wallet.

## Using the Autohydrater

In a terminal window, navigate to the location where you saved all the files. Run the `hydrate.py` file.

```bash
$ python hydrate.py
```

This terminal window will always need to remain open for the autohydrater to function.If the terminal window closes, just execute
`hydrate.py` again.

If this autohydrater helps you, consider supporting me by sending me an airdrop. 

*0xeDb0951cF765b6E19881497C407C39914D78c597*

If you haven't already joined the [animalfarm](https://theanimalfarm/referrals/0xeDb0951cF765b6E19881497C407C39914D78c597), then you should definitely have a look!