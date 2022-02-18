# web3

This Python script will automatically hydrate your DRIP when your available DRIP reaches 1% of your deposits.

Prerequisites:
Python3 Installed 

Packages:
web3, cryptography

1. Generate Fernet key to be used to encrypt private wallet key. Run this in a python terminal.

key = Fernet.generate_key().decode()

2. Add the key as an environment variable. This will allow you to query the key when the program runs.

os.environ['Fernet'] = key

3. Encrypt your private key. Open your MetaMask wallet or whatever wallet you use and find your private key. On MetaMask, this can be done by going to your account details and exporting the private key. Take your private key and replace PRIVATEKEYHERE with your key.

fernet = Fernet(key.encode())
encMessage = fernet.encrypt('PRIVATEKEYHERE'.encode()).decode()

4. Copy the encrypted message stored in the encMessage variable. An example of what this string looks like is below: 

gAAAAABiD8ygOfF4UDsV5tam4_HKj7fR9r49_ooNMa1NpHsAtk5spk_FJoiIh1hGn3wklXyDwUCMj1gEU5wXgAKutDmpfVe0SA==

5. Create a file called key.txt in the same directory that you have all of the .py files and add the encrypted key into the file. 

6. Open the price.py file and replace the wallet # on line 21 with your own

7. Open the hydrate.py file and replace the wallet # on line 5

## 8. In your terminal, run the hydrate.py file and 
