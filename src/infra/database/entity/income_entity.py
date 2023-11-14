from datetime import datetime

from beanie import Document
from pydantic import Field

class IncomeEntity(Document):
    user_id: str
    account_id: str
    value: float
    is_ignored: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)