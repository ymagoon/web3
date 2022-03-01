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

2. Once Python is installed, the following packages need to be installed.

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
>>>fernet = Fernet(key)
>>>encMessage = fernet.encrypt('YOURKEYHERE'.encode())
>>>encMessage.decode()
```

4. Take the value in `encMessage`, create a file called `key.txt` and save the text in the file 

5. Open `.env.example` and replace the key with the key you generated in step 3. Save the file without .example at the end. 

6. Open the `garden.py` file and replace the string stored in `wallet_public_addr` with your own public wallet.

7. Change the `plants_to_plant` value to the number of plants you want to compound after reaching

## Using the Autoplanter

In a terminal window, navigate to the location where you saved all the files. Run the `garden.py` file.

```bash
$ python garden.py
```

This terminal window will always need to remain open for the autoplanter to function. If the terminal window closes, just execute
`garden.py` again.

If this autoplanter helps you, consider supporting me by sending me an airdrop. 

**wallet:** *0xeDb0951cF765b6E19881497C407C39914D78c597*

If you haven't already invested in the [Animal Farm](https://theanimalfarm/referrals/0xeDb0951cF765b6E19881497C407C39914D78c597), then I highly recommend you doing so!