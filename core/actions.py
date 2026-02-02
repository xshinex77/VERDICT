from enum import Enum

class Action(Enum):
    CALL = "CALL"
    RETURN = "RETURN"
    REVERT = "REVERT"
    REVERT_CONTINUE = "REVERT_CONTINUE"
