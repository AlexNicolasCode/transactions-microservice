from dataclasses import dataclass

@dataclass
class SaveIncomeDTO:
    user_id: str
    account_id: str
    value: float
    is_ignored: bool