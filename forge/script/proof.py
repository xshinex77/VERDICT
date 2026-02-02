import hashlib

class ProofScheme:
    # 将来: "poseidon", "stark", "snark", "pqc"
    SHA256 = "sha256"
    POSEIDON = "poseidon"  # placeholder

def generate_proof(table_json: str, scheme: str) -> bytes:
    """
    Stubbed proof generator.
    - sha256: 実装済み
    - poseidon: 置き換え前提（I/F固定）
    """
    if scheme == ProofScheme.SHA256:
        return hashlib.sha256(table_json.encode()).digest()

    if scheme == ProofScheme.POSEIDON:
        # TODO: replace with poseidon(table_json)
        # Placeholder keeps interface stable
        return hashlib.sha256(b"POSEIDON::" + table_json.encode()).digest()

    raise ValueError("Unknown proof scheme")
