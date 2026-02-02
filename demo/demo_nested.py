from core.actions import Action
from core.verdict_table import VerdictEntry, VerdictTable
from anchor.eth_anchor import anchor_verdict

entries = [
    VerdictEntry(Action.CALL, "S0", "S1", "L1:ContractA"),
    VerdictEntry(Action.CALL, "S1", "S2", "L2:ContractB"),
    VerdictEntry(Action.REVERT, "S2", "S2", "L2:ContractB"),
    VerdictEntry(Action.REVERT_CONTINUE, "S2", "S1", "L1:ContractA"),
    VerdictEntry(Action.RETURN, "S1", "S0", "L1:ContractA"),
]

table = VerdictTable(entries)
result = table.evaluate()

if result == "REVERT":
    print("❌ VERDICT: REVERT — It never happened.")
else:
    h = anchor_verdict(str(entries))
    print("✅ VERDICT CONFIRMED:", h)
