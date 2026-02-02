from web3 import Web3
import os
import json
import hashlib

# ============
# Environment
# ============
RPC_URL = os.getenv("RPC_URL")
PK = os.getenv("PK")
ANCHOR_ADDR = os.getenv("ANCHOR_ADDR")

assert RPC_URL and PK and ANCHOR_ADDR, "Missing env vars"

w3 = Web3(Web3.HTTPProvider(RPC_URL))
anchor = Web3.to_checksum_address(ANCHOR_ADDR)

ABI = [
    {
        "inputs": [
            {"internalType": "bytes32", "name": "verdictHash", "type": "bytes32"},
            {"internalType": "bytes32", "name": "proofHash", "type": "bytes32"}
        ],
        "name": "confirm",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "internalType": "bytes32", "name": "verdictHash", "type": "bytes32"},
            {"indexed": False, "internalType": "bytes32", "name": "proofHash", "type": "bytes32"}
        ],
        "name": "VerdictConfirmed",
        "type": "event"
    }
]

contract = w3.eth.contract(address=anchor, abi=ABI)

# =====================
# VerdictTable
# =====================
verdict_table = {
    "case": "L2 → L1 nested call",
    "sequence": [
        "CALL B on L2",
        "CALL C on L1",
        "REVERT on L2",
        "REVERT_CONTINUE on L1"
    ],
    "final": "REVERT",
    "signature": {
        "scheme": "Dilithium",
        "pubkey": "0xPQC_PUBLIC_KEY_STUB",
        "sig": "0xPQC_SIGNATURE_STUB"
    }
}

verdict_table_json = json.dumps(
    verdict_table,
    sort_keys=True,
    separators=(",", ":")
)

# =====================
# Proof (stub)
# =====================
class ProofScheme:
    POSEIDON = "poseidon"

def h(b: bytes) -> bytes:
    return hashlib.sha256(b).digest()

def generate_proof(table_json: str) -> bytes:
    return h(b"POSEIDON::" + table_json.encode())

# =====================
# v0.3 Gas-Minimized Hash
# =====================
TABLE_DOMAIN = b"VERDICT::TABLE"
SIG_DOMAIN   = b"VERDICT::SIG"
FINAL_DOMAIN = b"VERDICT::FINAL"

table_root = h(TABLE_DOMAIN + verdict_table_json.encode())

sig_payload = json.dumps(
    verdict_table["signature"],
    sort_keys=True,
    separators=(",", ":")
).encode()
sig_root = h(SIG_DOMAIN + sig_payload)

verdict_hash = h(FINAL_DOMAIN + table_root + sig_root)
proof_hash = generate_proof(verdict_table_json)

# =====================
# On-chain confirm
# =====================
acct = w3.eth.accounts[0]

tx = contract.functions.confirm(
    verdict_hash,
    proof_hash
).build_transaction({
    "from": acct,
    "nonce": w3.eth.get_transaction_count(acct),
    "gas": 150000,
    "gasPrice": w3.to_wei("1", "gwei"),
    "chainId": 31337
})

signed = w3.eth.account.sign_transaction(tx, private_key=PK)
txh = w3.eth.send_raw_transaction(signed.raw_transaction)

print("🧑‍⚖️ VERDICT FLOW COMPLETE (v0.3)")
print("VerdictHash :", verdict_hash.hex())
print("ProofHash   :", proof_hash.hex())
print("TX          :", txh.hex())

