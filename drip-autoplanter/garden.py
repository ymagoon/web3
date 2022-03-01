import json
import time
from datetime import datetime
from datetime import timedelta
import math
import contract as c

garden_contract_addr = "0x685BFDd3C2937744c13d7De0821c83191E3027FF"
wallet_public_addr = "0xeDb0951cF765b6E19881497C407C39914D78c597"

# load private key
wallet_private_key = open('key.txt', "r").readline()

# load abi
f = open('garden_abi.json')
garden_abi = json.load(f)

# create contract
garden_contract = c.connect_to_contract(garden_contract_addr, garden_abi)

def calculate_seed_to_lp(seeds):
    return garden_contract.functions.calculateSeedSell(seeds).call()/1000000000000000000

def get_time_multiplier():
    return garden_contract.functions.currentTimeMultiplier().call()/1000000000

def get_garden_balance():
    return garden_contract.functions.getBalance().call()/1000000000000000000

def get_total_seeds():
    return garden_contract.functions.marketSeeds().call()

def get_user_seeds(addr):
    return garden_contract.functions.getUserSeeds(addr).call()

def get_plants_planted(addr):
    return garden_contract.functions.hatcheryPlants(addr).call()

def get_seed_to_lp_ratio(addr):
    total_seeds = get_user_seeds(addr)
    total_lp = calculate_seed_to_lp(total_seeds)
    return total_lp *.95 # tax of 5% on withdrawls

def calculate_next_plant(plants_needed):
    seeds = get_user_seeds(wallet_public_addr)
    total_plants = get_plants_planted(wallet_public_addr)
    
    # each plant generates 1 seed per second
    seeds_per_second = total_plants
    seed_remainder = seeds % 2592000
    seeds_needed = (plants_needed * 2592000) - seed_remainder
    
    time_remaining = seeds_needed / seeds_per_second
    return int(time_remaining)

def plant():
    txn = garden_contract.functions.plantSeeds(c.dev()).buildTransaction(c.get_tx_options(wallet_public_addr, 500000))
    return c.send_txn(txn, wallet_private_key)

plants_to_plant = 1

while True:
    seeds = get_user_seeds(wallet_public_addr)
    total_plants = get_plants_planted(wallet_public_addr)
    new_plants = math.floor(seeds / 2592000)
    seed_remainder = seeds % 2592000
    
    # calculate % of seeds lost 
    seed_ratio = (1 - (seed_remainder / 2592000))
    
    # this prevents loss of seeds to under 8000 per planting
    seed_range = True if seed_ratio > .997 else False

    if new_plants >= plants_to_plant and seed_range:
        plant()
        
        print(f'Planted! {new_plants} added to your garden. Total number of plants now {total_plants + new_plants}')
        print(f'Seeds lost: {seed_remainder}')
        
        time.sleep(5) # prevent nonce error from being thrown
    else:
        # if referral adds more plants than we are compounding
        if plants_to_plant >= new_plants:
            plants_needed = plants_to_plant - new_plants
        else:
            plants_needed = new_plants + 1
            
        seeds_needed = (plants_needed * 2592000) - seed_remainder
  
        print(f"Planting not ready {seeds} seeds available. Need {seeds_needed} more")
        
        # calculate time remaining in seconds
        time_remaining = calculate_next_plant(plants_needed)
        
        for second in range(0, time_remaining, 1):
            t = time_remaining - second
            # poll every 30 seconds to see if referrals have been paid
            if t % 30 == 0:
                break

            print(f"Next Plant Ready: {str(timedelta(seconds=t)).split(':')[0]} hours {str(timedelta(seconds=t)).split(':')[1]} min {str(timedelta(seconds=t)).split(':')[2]} seconds",end="\r")
            time.sleep(1)