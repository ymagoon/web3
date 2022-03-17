import argparse
import configparser
import json
import math
import contract as c
import time
from datetime import timedelta


def calculate_seed_to_lp(seeds):
    return garden_contract.functions.calculateSeedSell(seeds)\
        .call()/1000000000000000000


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
    return total_lp * .95  # tax of 5% on withdrawls


def calculate_next_plant(plants_needed):
    seeds = get_user_seeds(wallet_address)
    total_plants = get_plants_planted(wallet_address)

    # each plant generates 1 seed per second
    seeds_per_second = total_plants
    seed_remainder = seeds % 2592000
    seeds_needed = (plants_needed * 2592000) - seed_remainder

    time_remaining = seeds_needed / seeds_per_second
    return int(time_remaining)


def plant():
    txn = garden_contract.functions.plantSeeds(c.dev(wallet_address))\
        .buildTransaction(c.get_tx_options(wallet_address, 500000))
    return c.send_txn(txn, wallet_private_key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Drip Autoplanter')
    parser.add_argument(
        "-w", "--wallet-address",
        help="Your wallet address",
        type=str, dest='wallet_address',
        required=True
    )
    parser.add_argument(
        "-p", "--plants-to-compound",
        help="Number of plants to compound. Defaults to plants grown a day",
        type=int,
        dest='plants_to_compound',
    )
    parser.add_argument(
        "-f", "--force-compound",
        help="Ignore seeds lost",
        action='store_true',
        dest='force_compound',
    )
    args = parser.parse_args()

    # load config
    config = configparser.ConfigParser()
    config.read('config.ini')
    garden_contract_addr = config['DEFAULT']['garden_contract_address']

    # load private key
    wallet_private_key = open('key.txt', "r").readline()

    # load abi
    f = open('garden_abi.json')
    garden_abi = json.load(f)

    # create contract
    garden_contract = c.connect_to_contract(garden_contract_addr, garden_abi)

    # Process arguments
    wallet_address = args.wallet_address
    force_compound = args.force_compound
    if args.plants_to_compound:
        plants_to_compound = args.plants_to_compound
    else:
        plants_to_compound = \
            int((get_plants_planted(wallet_address) * 86400) / 2592000)

    print(f'Program will compound {plants_to_compound} plant when ready.' +
          f'Force compound is {force_compound}')

    while True:
        seeds = get_user_seeds(wallet_address)
        total_plants = get_plants_planted(wallet_address)
        new_plants = math.floor(seeds / 2592000)
        seed_remainder = seeds % 2592000

        # calculate % of seeds lost
        seed_ratio = (1 - (seed_remainder / 2592000))

        # If loss of seeds is under 8000 this will be true
        seed_range = True if seed_ratio > .997 else False

        print(f'Currently you have {new_plants} new plants and {seeds} seeds')

        if new_plants >= plants_to_compound and (seed_range or force_compound):
            plant()

            print(f'Planted! {new_plants} added to your garden. Total number of plants now {total_plants + new_plants}')
            print(f'Seeds lost: {seed_remainder}')

            time.sleep(5)  # prevent nonce error from being thrown
        else:
            # if referral adds more plants than we are compounding
            if plants_to_compound > new_plants:
                plants_needed = plants_to_compound - new_plants
            else:
                plants_needed = 1

            seeds_needed = (plants_needed * 2592000) - seed_remainder

            print(f"Planting not ready {seeds} seeds available. Need {seeds_needed} more")

            # calculate time remaining in seconds
            time_remaining = calculate_next_plant(plants_needed)

            for second in range(0, time_remaining, 1):
                t = time_remaining - second
                # poll every 30 seconds to see if referrals have been paid
                if t % 30 == 0:
                    break

                print(f"Next Plant Ready: {str(timedelta(seconds=t)).split(':')[0]} hours {str(timedelta(seconds=t)).split(':')[1]} min {str(timedelta(seconds=t)).split(':')[2]} seconds", end="\r")
                time.sleep(.5)
