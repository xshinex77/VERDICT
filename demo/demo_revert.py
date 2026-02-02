from core.actions import Action
from core.verdict_table import VerdictEntry, VerdictTable
from anchor.eth_anchor import anchor_verdict

entries = [
    VerdictEntry(Action.CALL, "S0", "S1", "SystemA"),
    VerdictEntry(Action.REVERT, "S1", "S1", "SystemB"),
]

table = VerdictTable(entries)

if not table.is_atomic():
    print("❌ VERDICT: REVERT — It never happened.")
else:
    h = anchor_verdict(str(table))
    print("✅ VERDICT CONFIRMED:", h)
