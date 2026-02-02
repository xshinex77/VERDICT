# VERDICT

If VERDICT says no, it never happened.

VERDICT is an execution-free finality layer.
It does not execute transactions.
It finalizes meaning.

There is no execution, only proof.
REVERT is global.
Ethereum is the final court.

Execution can be faked.
Logs can be ignored.
Finality cannot.

Architecture:
VerdictTable → Proof → Ethereum Anchor

Status:
- Nested REVERT semantics: implemented
- Ethereum anchoring: implemented
- ZK-proof interface: stubbed

Implementation note:
VERDICT uses Foundry only as a deterministic toolchain to anchor finality on Ethereum.
Forge compiles and deploys the anchor, Anvil provides a local court, and Cast is used solely to verify verdict logs.
No business logic is executed on-chain.
