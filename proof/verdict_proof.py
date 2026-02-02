import hashlib

def generate_proof(verdict_table: str) -> str:
    """
    ZK proof stub.
    In v0, proof == hash(verdict_table)
    """
    return hashlib.sha256(verdict_table.encode()).hexdigest()

def verify_proof(verdict_table: str, proof: str) -> bool:
    return generate_proof(verdict_table) == proof
