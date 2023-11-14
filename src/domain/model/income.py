import datetime
from dataclasses import dataclass

@dataclass
class Income:
    id: str
    user_id: str
    account_id: str
    value: float
    is_ignored: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime