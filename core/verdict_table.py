from dataclasses import dataclass
from typing import List
from core.actions import Action

@dataclass
class VerdictEntry:
    action: Action
    state_before: str
    state_after: str
    target: str

@dataclass
class VerdictTable:
    entries: List[VerdictEntry]

    def evaluate(self) -> str:
        """
        Returns final VERDICT state.
        """
        reverted = False

        for e in self.entries:
            if e.action == Action.REVERT:
                reverted = True
                print(f"⚠️ REVERT issued by {e.target}")
            elif e.action == Action.REVERT_CONTINUE:
                if reverted:
                    print(f"↩️ REVERT_CONTINUE acknowledged by {e.target}")
                    reverted = False

        if reverted:
            return "REVERT"
        return "CONFIRMED"
