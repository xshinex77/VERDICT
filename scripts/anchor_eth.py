from web3 import Web3
import os

RPC_URL = os.getenv("RPC_URL")
PK = os.getenv("PK")
ANCHOR_ADDR = os.getenv("ANCHOR_ADDR")

assert RPC_URL and PK and ANCHOR_ADDR, "Missing env vars"

w3 = Web3(Web3.HTTPProvider(RPC_URL))
addr = Web3.to_checksum_address(ANCHOR_ADDR)

# ✅ function + event を含む完全ABI
abi = [
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "verdictHash",
                "type": "bytes32"
            }
        ],
        "name": "confirm",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "verdictHash",
                "type": "bytes32"
            }
        ],
        "name": "VerdictConfirmed",
        "type": "event"
    }
]

contract = w3.eth.contract(address=addr, abi=abi)

# VERDICT の「判決ハッシュ」
verdict_hex = "e1a2bc924f4b7df6d0f97b64dd520760b81c82198c2daebb6cd15129be34c93a"
verdict = bytes.fromhex(verdict_hex)

acct = w3.eth.accounts[0]

tx = contract.functions.confirm(verdict).build_transaction({
    "from": acct,
    "nonce": w3.eth.get_transaction_count(acct),
    "gas": 100000,
    "gasPrice": w3.to_wei("1", "gwei"),
    "chainId": 31337
})

signed = w3.eth.account.sign_transaction(tx, private_key=PK)
txh = w3.eth.send_raw_transaction(signed.raw_transaction)

print("🧑‍⚖️ VERDICT ANCHORED TX:", txh.hex())
