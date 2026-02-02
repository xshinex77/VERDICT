# VERDICT

If VERDICT says no, it never happened.

VERDICT is an execution-free finality layer for Ethereum.
It does not execute transactions.
It anchors meaning.

There is no execution, only proof.
REVERT is global.
Ethereum is the final court.

Execution can be faked.
Logs can be ignored.
Finality cannot.

## Architecture
VerdictTable → Proof → Ethereum Anchor

## Status
- Nested REVERT semantics: implemented
- Ethereum anchoring: implemented
- ZK-proof interface: stubbed

## Design Notes
VERDICT uses Ethereum only as a final court of record.
No business logic is executed on-chain.
All proofs and verification are performed off-chain by observers.
