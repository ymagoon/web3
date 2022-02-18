import os
from web3 import Web3
from cryptography.fernet import Fernet

RPC_Url = "https://bsc-dataseed.binance.org:443"
web3 = Web3(Web3.HTTPProvider(RPC_Url))

faucet = {"0xFFE811714ab35360b67eE195acE7C10D93f89D8C": [{"anonymous": False, "inputs": [
    {"indexed": True, "internalType": "address", "name": "_src", "type": "address"},
    {"indexed": True, "internalType": "address", "name": "_dest", "type": "address"},
    {"indexed": False, "internalType": "uint256", "name": "_deposits", "type": "uint256"},
    {"indexed": False, "internalType": "uint256", "name": "_payouts", "type": "uint256"}], "name": "BalanceTransfer",
                                                          "type": "event"}, {"anonymous": False, "inputs": [
    {"indexed": True, "internalType": "address", "name": "addr", "type": "address"},
    {"indexed": True, "internalType": "address", "name": "beneficiary", "type": "address"}],
                                                                             "name": "BeneficiaryUpdate",
                                                                             "type": "event"}, {"anonymous": False,
                                                                                                "inputs": [
                                                                                                    {"indexed": True,
                                                                                                     "internalType": "address",
                                                                                                     "name": "addr",
                                                                                                     "type": "address"},
                                                                                                    {"indexed": False,
                                                                                                     "internalType": "uint256",
                                                                                                     "name": "timestamp",
                                                                                                     "type": "uint256"}],
                                                                                                "name": "Checkin",
                                                                                                "type": "event"},
                                                         {"anonymous": False, "inputs": [
                                                             {"indexed": True, "internalType": "address",
                                                              "name": "addr", "type": "address"},
                                                             {"indexed": True, "internalType": "address",
                                                              "name": "from", "type": "address"},
                                                             {"indexed": False, "internalType": "uint256",
                                                              "name": "amount", "type": "uint256"}],
                                                          "name": "DirectPayout", "type": "event"}, {"anonymous": False,
                                                                                                     "inputs": [{
                                                                                                                    "indexed": True,
                                                                                                                    "internalType": "address",
                                                                                                                    "name": "addr",
                                                                                                                    "type": "address"},
                                                                                                                {
                                                                                                                    "indexed": False,
                                                                                                                    "internalType": "uint256",
                                                                                                                    "name": "timestamp",
                                                                                                                    "type": "uint256"}],
                                                                                                     "name": "HeartBeat",
                                                                                                     "type": "event"},
                                                         {"anonymous": False, "inputs": [
                                                             {"indexed": True, "internalType": "address",
                                                              "name": "addr", "type": "address"},
                                                             {"indexed": False, "internalType": "uint256",
                                                              "name": "interval", "type": "uint256"}],
                                                          "name": "HeartBeatIntervalUpdate", "type": "event"},
                                                         {"anonymous": False, "inputs": [
                                                             {"indexed": True, "internalType": "address",
                                                              "name": "addr", "type": "address"},
                                                             {"indexed": False, "internalType": "uint256",
                                                              "name": "referrals", "type": "uint256"},
                                                             {"indexed": False, "internalType": "uint256",
                                                              "name": "total_deposits", "type": "uint256"},
                                                             {"indexed": False, "internalType": "uint256",
                                                              "name": "total_payouts", "type": "uint256"},
                                                             {"indexed": False, "internalType": "uint256",
                                                              "name": "total_structure", "type": "uint256"}],
                                                          "name": "Leaderboard", "type": "event"}, {"anonymous": False,
                                                                                                    "inputs": [{
                                                                                                                   "indexed": True,
                                                                                                                   "internalType": "address",
                                                                                                                   "name": "addr",
                                                                                                                   "type": "address"},
                                                                                                               {
                                                                                                                   "indexed": False,
                                                                                                                   "internalType": "uint256",
                                                                                                                   "name": "amount",
                                                                                                                   "type": "uint256"}],
                                                                                                    "name": "LimitReached",
                                                                                                    "type": "event"},
                                                         {"anonymous": False, "inputs": [
                                                             {"indexed": True, "internalType": "address",
                                                              "name": "addr", "type": "address"},
                                                             {"indexed": True, "internalType": "address",
                                                              "name": "manager", "type": "address"},
                                                             {"indexed": False, "internalType": "uint256",
                                                              "name": "timestamp", "type": "uint256"}],
                                                          "name": "ManagerUpdate", "type": "event"},
                                                         {"anonymous": False, "inputs": [
                                                             {"indexed": True, "internalType": "address",
                                                              "name": "addr", "type": "address"},
                                                             {"indexed": True, "internalType": "address",
                                                              "name": "from", "type": "address"},
                                                             {"indexed": False, "internalType": "uint256",
                                                              "name": "amount", "type": "uint256"}],
                                                          "name": "MatchPayout", "type": "event"}, {"anonymous": False,
                                                                                                    "inputs": [{
                                                                                                                   "indexed": True,
                                                                                                                   "internalType": "address",
                                                                                                                   "name": "from",
                                                                                                                   "type": "address"},
                                                                                                               {
                                                                                                                   "indexed": True,
                                                                                                                   "internalType": "address",
                                                                                                                   "name": "to",
                                                                                                                   "type": "address"},
                                                                                                               {
                                                                                                                   "indexed": False,
                                                                                                                   "internalType": "uint256",
                                                                                                                   "name": "amount",
                                                                                                                   "type": "uint256"},
                                                                                                               {
                                                                                                                   "indexed": False,
                                                                                                                   "internalType": "uint256",
                                                                                                                   "name": "timestamp",
                                                                                                                   "type": "uint256"}],
                                                                                                    "name": "NewAirdrop",
                                                                                                    "type": "event"},
                                                         {"anonymous": False, "inputs": [
                                                             {"indexed": True, "internalType": "address",
                                                              "name": "addr", "type": "address"},
                                                             {"indexed": False, "internalType": "uint256",
                                                              "name": "amount", "type": "uint256"}],
                                                          "name": "NewDeposit", "type": "event"}, {"anonymous": False,
                                                                                                   "inputs": [
                                                                                                       {"indexed": True,
                                                                                                        "internalType": "address",
                                                                                                        "name": "previousOwner",
                                                                                                        "type": "address"},
                                                                                                       {"indexed": True,
                                                                                                        "internalType": "address",
                                                                                                        "name": "newOwner",
                                                                                                        "type": "address"}],
                                                                                                   "name": "OwnershipTransferred",
                                                                                                   "type": "event"},
                                                         {"anonymous": False, "inputs": [
                                                             {"indexed": True, "internalType": "address",
                                                              "name": "addr", "type": "address"},
                                                             {"indexed": True, "internalType": "address",
                                                              "name": "upline", "type": "address"}], "name": "Upline",
                                                          "type": "event"}, {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "addr", "type": "address"},
        {"indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "Withdraw",
                                                                             "type": "event"},
                                                         {"stateMutability": "payable", "type": "fallback"},
                                                         {"inputs": [], "name": "CompoundTax", "outputs": [
                                                             {"internalType": "uint256", "name": "",
                                                              "type": "uint256"}], "stateMutability": "view",
                                                          "type": "function"}, {"inputs": [], "name": "ExitTax",
                                                                                "outputs": [{"internalType": "uint256",
                                                                                             "name": "",
                                                                                             "type": "uint256"}],
                                                                                "stateMutability": "view",
                                                                                "type": "function"},
                                                         {"inputs": [], "name": "MAX_UINT", "outputs": [
                                                             {"internalType": "uint256", "name": "",
                                                              "type": "uint256"}], "stateMutability": "view",
                                                          "type": "function"}, {"inputs": [
        {"internalType": "address", "name": "_to", "type": "address"},
        {"internalType": "uint256", "name": "_amount", "type": "uint256"}], "name": "airdrop", "outputs": [],
                                                                                "stateMutability": "nonpayable",
                                                                                "type": "function"}, {"inputs": [
        {"internalType": "address", "name": "", "type": "address"}], "name": "airdrops", "outputs": [
        {"internalType": "uint256", "name": "airdrops", "type": "uint256"},
        {"internalType": "uint256", "name": "airdrops_received", "type": "uint256"},
        {"internalType": "uint256", "name": "last_airdrop", "type": "uint256"}], "stateMutability": "view",
                                                                                                      "type": "function"},
                                                         {"inputs": [{"internalType": "address", "name": "_addr",
                                                                      "type": "address"}], "name": "balanceLevel",
                                                          "outputs": [
                                                              {"internalType": "uint8", "name": "", "type": "uint8"}],
                                                          "stateMutability": "view", "type": "function"},
                                                         {"inputs": [], "name": "checkin", "outputs": [],
                                                          "stateMutability": "nonpayable", "type": "function"},
                                                         {"inputs": [], "name": "claim", "outputs": [],
                                                          "stateMutability": "nonpayable", "type": "function"}, {
                                                             "inputs": [{"internalType": "address", "name": "_addr",
                                                                         "type": "address"}], "name": "claimsAvailable",
                                                             "outputs": [{"internalType": "uint256", "name": "",
                                                                          "type": "uint256"}],
                                                             "stateMutability": "view", "type": "function"},
                                                         {"inputs": [], "name": "contractInfo", "outputs": [
                                                             {"internalType": "uint256", "name": "_total_users",
                                                              "type": "uint256"},
                                                             {"internalType": "uint256", "name": "_total_deposited",
                                                              "type": "uint256"},
                                                             {"internalType": "uint256", "name": "_total_withdraw",
                                                              "type": "uint256"},
                                                             {"internalType": "uint256", "name": "_total_bnb",
                                                              "type": "uint256"},
                                                             {"internalType": "uint256", "name": "_total_txs",
                                                              "type": "uint256"},
                                                             {"internalType": "uint256", "name": "_total_airdrops",
                                                              "type": "uint256"}], "stateMutability": "view",
                                                          "type": "function"}, {"inputs": [
        {"internalType": "address", "name": "_addr", "type": "address"}], "name": "creditsAndDebits", "outputs": [
        {"internalType": "uint256", "name": "_credits", "type": "uint256"},
        {"internalType": "uint256", "name": "_debits", "type": "uint256"}], "stateMutability": "view",
                                                                                "type": "function"}, {"inputs": [
        {"internalType": "address", "name": "", "type": "address"}], "name": "custody", "outputs": [
        {"internalType": "address", "name": "manager", "type": "address"},
        {"internalType": "address", "name": "beneficiary", "type": "address"},
        {"internalType": "uint256", "name": "last_heartbeat", "type": "uint256"},
        {"internalType": "uint256", "name": "last_checkin", "type": "uint256"},
        {"internalType": "uint256", "name": "heartbeat_interval", "type": "uint256"}], "stateMutability": "view",
                                                                                                      "type": "function"},
                                                         {"inputs": [{"internalType": "address", "name": "_upline",
                                                                      "type": "address"},
                                                                     {"internalType": "uint256", "name": "_amount",
                                                                      "type": "uint256"}], "name": "deposit",
                                                          "outputs": [], "stateMutability": "nonpayable",
                                                          "type": "function"},
                                                         {"inputs": [], "name": "deposit_bracket_size", "outputs": [
                                                             {"internalType": "uint256", "name": "",
                                                              "type": "uint256"}], "stateMutability": "view",
                                                          "type": "function"},
                                                         {"inputs": [], "name": "dripVaultAddress", "outputs": [
                                                             {"internalType": "address", "name": "",
                                                              "type": "address"}], "stateMutability": "view",
                                                          "type": "function"}, {"inputs": [
        {"internalType": "address", "name": "_addr", "type": "address"}], "name": "getCustody", "outputs": [
        {"internalType": "address", "name": "_beneficiary", "type": "address"},
        {"internalType": "uint256", "name": "_heartbeat_interval", "type": "uint256"},
        {"internalType": "address", "name": "_manager", "type": "address"}], "stateMutability": "view",
                                                                                "type": "function"},
                                                         {"inputs": [], "name": "initialize", "outputs": [],
                                                          "stateMutability": "nonpayable", "type": "function"}, {
                                                             "inputs": [{"internalType": "address", "name": "_addr",
                                                                         "type": "address"},
                                                                        {"internalType": "uint8", "name": "_level",
                                                                         "type": "uint8"}], "name": "isBalanceCovered",
                                                             "outputs": [
                                                                 {"internalType": "bool", "name": "", "type": "bool"}],
                                                             "stateMutability": "view", "type": "function"}, {
                                                             "inputs": [{"internalType": "address", "name": "_addr",
                                                                         "type": "address"}], "name": "isNetPositive",
                                                             "outputs": [
                                                                 {"internalType": "bool", "name": "", "type": "bool"}],
                                                             "stateMutability": "view", "type": "function"}, {
                                                             "inputs": [{"internalType": "address", "name": "_addr",
                                                                         "type": "address"}], "name": "lastActivity",
                                                             "outputs": [
                                                                 {"internalType": "uint256", "name": "_heartbeat",
                                                                  "type": "uint256"}, {"internalType": "uint256",
                                                                                       "name": "_lapsed_heartbeat",
                                                                                       "type": "uint256"},
                                                                 {"internalType": "uint256", "name": "_checkin",
                                                                  "type": "uint256"},
                                                                 {"internalType": "uint256", "name": "_lapsed_checkin",
                                                                  "type": "uint256"}], "stateMutability": "view",
                                                             "type": "function"}, {"inputs": [
        {"internalType": "uint256", "name": "_amount", "type": "uint256"}], "name": "maxPayoutOf", "outputs": [
        {"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "pure", "type": "function"},
                                                         {"inputs": [], "name": "max_payout_cap", "outputs": [
                                                             {"internalType": "uint256", "name": "",
                                                              "type": "uint256"}], "stateMutability": "view",
                                                          "type": "function"}, {"inputs": [], "name": "owner",
                                                                                "outputs": [{"internalType": "address",
                                                                                             "name": "",
                                                                                             "type": "address"}],
                                                                                "stateMutability": "view",
                                                                                "type": "function"}, {"inputs": [
        {"internalType": "address", "name": "_addr", "type": "address"}], "name": "payoutOf", "outputs": [
        {"internalType": "uint256", "name": "payout", "type": "uint256"},
        {"internalType": "uint256", "name": "max_payout", "type": "uint256"},
        {"internalType": "uint256", "name": "net_payout", "type": "uint256"},
        {"internalType": "uint256", "name": "sustainability_fee", "type": "uint256"}], "stateMutability": "view",
                                                                                                      "type": "function"},
                                                         {"inputs": [{"internalType": "uint256", "name": "",
                                                                      "type": "uint256"}], "name": "ref_balances",
                                                          "outputs": [{"internalType": "uint256", "name": "",
                                                                       "type": "uint256"}], "stateMutability": "view",
                                                          "type": "function"},
                                                         {"inputs": [], "name": "renounceOwnership", "outputs": [],
                                                          "stateMutability": "nonpayable", "type": "function"},
                                                         {"inputs": [], "name": "roll", "outputs": [],
                                                          "stateMutability": "nonpayable", "type": "function"}, {
                                                             "inputs": [{"internalType": "address", "name": "_addr",
                                                                         "type": "address"}, {"internalType": "uint256",
                                                                                              "name": "_pendingDiv",
                                                                                              "type": "uint256"}],
                                                             "name": "sustainabilityFeeV2", "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
                                                         {"inputs": [], "name": "total_airdrops", "outputs": [
                                                             {"internalType": "uint256", "name": "",
                                                              "type": "uint256"}], "stateMutability": "view",
                                                          "type": "function"}, {"inputs": [], "name": "total_bnb",
                                                                                "outputs": [{"internalType": "uint256",
                                                                                             "name": "",
                                                                                             "type": "uint256"}],
                                                                                "stateMutability": "view",
                                                                                "type": "function"},
                                                         {"inputs": [], "name": "total_deposited", "outputs": [
                                                             {"internalType": "uint256", "name": "",
                                                              "type": "uint256"}], "stateMutability": "view",
                                                          "type": "function"}, {"inputs": [], "name": "total_txs",
                                                                                "outputs": [{"internalType": "uint256",
                                                                                             "name": "",
                                                                                             "type": "uint256"}],
                                                                                "stateMutability": "view",
                                                                                "type": "function"},
                                                         {"inputs": [], "name": "total_users", "outputs": [
                                                             {"internalType": "uint256", "name": "",
                                                              "type": "uint256"}], "stateMutability": "view",
                                                          "type": "function"}, {"inputs": [], "name": "total_withdraw",
                                                                                "outputs": [{"internalType": "uint256",
                                                                                             "name": "",
                                                                                             "type": "uint256"}],
                                                                                "stateMutability": "view",
                                                                                "type": "function"}, {"inputs": [
        {"internalType": "address", "name": "newOwner", "type": "address"}], "name": "transferOwnership", "outputs": [],
                                                                                                      "stateMutability": "nonpayable",
                                                                                                      "type": "function"},
                                                         {"inputs": [
                                                             {"internalType": "uint256", "name": "_newCompoundTax",
                                                              "type": "uint256"}], "name": "updateCompoundTax",
                                                          "outputs": [], "stateMutability": "nonpayable",
                                                          "type": "function"}, {"inputs": [
        {"internalType": "uint256", "name": "_newBracketSize", "type": "uint256"}], "name": "updateDepositBracketSize",
                                                                                "outputs": [],
                                                                                "stateMutability": "nonpayable",
                                                                                "type": "function"}, {"inputs": [
        {"internalType": "uint256", "name": "_newExitTax", "type": "uint256"}], "name": "updateExitTax", "outputs": [],
                                                                                                      "stateMutability": "nonpayable",
                                                                                                      "type": "function"},
                                                         {"inputs": [
                                                             {"internalType": "uint256[]", "name": "_newRefBalances",
                                                              "type": "uint256[]"}], "name": "updateHoldRequirements",
                                                          "outputs": [], "stateMutability": "nonpayable",
                                                          "type": "function"}, {"inputs": [
        {"internalType": "uint256", "name": "_newInitialDeposit", "type": "uint256"}], "name": "updateInitialDeposit",
                                                                                "outputs": [],
                                                                                "stateMutability": "nonpayable",
                                                                                "type": "function"}, {"inputs": [
        {"internalType": "uint256", "name": "_newPayoutCap", "type": "uint256"}], "name": "updateMaxPayoutCap",
                                                                                                      "outputs": [],
                                                                                                      "stateMutability": "nonpayable",
                                                                                                      "type": "function"},
                                                         {"inputs": [
                                                             {"internalType": "uint256", "name": "_newPayoutRate",
                                                              "type": "uint256"}], "name": "updatePayoutRate",
                                                          "outputs": [], "stateMutability": "nonpayable",
                                                          "type": "function"}, {"inputs": [
        {"internalType": "uint256", "name": "_newRefBonus", "type": "uint256"}], "name": "updateRefBonus",
                                                                                "outputs": [],
                                                                                "stateMutability": "nonpayable",
                                                                                "type": "function"}, {"inputs": [
        {"internalType": "uint256", "name": "_newRefDepth", "type": "uint256"}], "name": "updateRefDepth",
                                                                                                      "outputs": [],
                                                                                                      "stateMutability": "nonpayable",
                                                                                                      "type": "function"},
                                                         {"inputs": [{"internalType": "address", "name": "_addr",
                                                                      "type": "address"}], "name": "userInfo",
                                                          "outputs": [{"internalType": "address", "name": "upline",
                                                                       "type": "address"}, {"internalType": "uint256",
                                                                                            "name": "deposit_time",
                                                                                            "type": "uint256"},
                                                                      {"internalType": "uint256", "name": "deposits",
                                                                       "type": "uint256"},
                                                                      {"internalType": "uint256", "name": "payouts",
                                                                       "type": "uint256"}, {"internalType": "uint256",
                                                                                            "name": "direct_bonus",
                                                                                            "type": "uint256"},
                                                                      {"internalType": "uint256", "name": "match_bonus",
                                                                       "type": "uint256"}, {"internalType": "uint256",
                                                                                            "name": "last_airdrop",
                                                                                            "type": "uint256"}],
                                                          "stateMutability": "view", "type": "function"}, {"inputs": [
        {"internalType": "address", "name": "_addr", "type": "address"}], "name": "userInfoTotals", "outputs": [
        {"internalType": "uint256", "name": "referrals", "type": "uint256"},
        {"internalType": "uint256", "name": "total_deposits", "type": "uint256"},
        {"internalType": "uint256", "name": "total_payouts", "type": "uint256"},
        {"internalType": "uint256", "name": "total_structure", "type": "uint256"},
        {"internalType": "uint256", "name": "airdrops_total", "type": "uint256"},
        {"internalType": "uint256", "name": "airdrops_received", "type": "uint256"}], "stateMutability": "view",
                                                                                                           "type": "function"},
                                                         {"inputs": [{"internalType": "address", "name": "",
                                                                      "type": "address"}], "name": "users", "outputs": [
                                                             {"internalType": "address", "name": "upline",
                                                              "type": "address"},
                                                             {"internalType": "uint256", "name": "referrals",
                                                              "type": "uint256"},
                                                             {"internalType": "uint256", "name": "total_structure",
                                                              "type": "uint256"},
                                                             {"internalType": "uint256", "name": "direct_bonus",
                                                              "type": "uint256"},
                                                             {"internalType": "uint256", "name": "match_bonus",
                                                              "type": "uint256"},
                                                             {"internalType": "uint256", "name": "deposits",
                                                              "type": "uint256"},
                                                             {"internalType": "uint256", "name": "deposit_time",
                                                              "type": "uint256"},
                                                             {"internalType": "uint256", "name": "payouts",
                                                              "type": "uint256"},
                                                             {"internalType": "uint256", "name": "rolls",
                                                              "type": "uint256"},
                                                             {"internalType": "uint256", "name": "ref_claim_pos",
                                                              "type": "uint256"},
                                                             {"internalType": "uint256", "name": "accumulatedDiv",
                                                              "type": "uint256"}], "stateMutability": "view",
                                                          "type": "function"}]}


def connect_to_contract(contract_creds):
    contract_list = [[key, value] for key, value in contract_creds.items()][0]
    contract = web3.eth.contract(address=contract_list[0], abi=contract_list[1])
    return contract


def sendTxn(txn, wallet_key):
    FERNETKEYHERE = os.environ['Fernet']
    ENCRYPTEDSTRINGHERE = wallet_key
    
    txn_signed = web3.eth.account.signTransaction(txn, private_key=Fernet(FERNETKEYHERE.encode()).decrypt(
        ENCRYPTEDSTRINGHERE.encode()).decode())
    tx_hash = web3.eth.sendRawTransaction(txn_signed.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    return tx_receipt


def getTxOptions(Wallet_PublicAddress, gas=500000):
    return {
        "nonce": web3.eth.getTransactionCount(Wallet_PublicAddress),
        "from": Wallet_PublicAddress,
        "gas": gas,
        "gasPrice": web3.toWei(5, "gwei")
    }
