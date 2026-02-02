import argparse
import json
import hashlib
import sys

# =========
# Hash util
# =========
def h(b: bytes) -> bytes:
    return hashlib.sha256(b).digest()

TABLE_DOMAIN = b"VERDICT::TABLE"
SIG_DOMAIN   = b"VERDICT::SIG"
FINAL_DOMAIN = b"VERDICT::FINAL"

# =========
# CLI args
# =========
ap = argparse.ArgumentParser(description="VERDICT Observer Verifier")
ap.add_argument("--table", required=True, help="VerdictTable JSON file")
ap.add_argument("--verdict-hash", required=True, help="On-chain verdictHash (hex)")
args = ap.parse_args()

# =========
# Load table
# =========
with open(args.table, "r") as f:
    verdict_table = json.load(f)

table_json = json.dumps(
    verdict_table,
    sort_keys=True,
    separators=(",", ":")
)

# =========
# Recompute roots
# =========
table_root = h(TABLE_DOMAIN + table_json.encode())

sig_payload = json.dumps(
    verdict_table.get("signature", {}),
    sort_keys=True,
    separators=(",", ":")
).encode()
sig_root = h(SIG_DOMAIN + sig_payload)

recomputed_verdict = h(FINAL_DOMAIN + table_root + sig_root).hex()

# =========
# Compare
# =========
onchain_verdict = args.verdict_hash.lower().removeprefix("0x")

print("=== VERDICT OBSERVER ===")
print("TableRoot   :", table_root.hex())
print("SigRoot     :", sig_root.hex())
print("Recomputed  :", recomputed_verdict)
print("On-chain    :", onchain_verdict)

if recomputed_verdict == onchain_verdict:
    print("✅ VERDICT MATCH — It really happened.")
    sys.exit(0)
else:
    print("❌ VERDICT MISMATCH — It never happened.")
    sys.exit(1)

