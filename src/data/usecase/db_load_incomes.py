from typing import List

from src.domain.model.income import Income
from src.domain.usecase.load_incomes import LoadIncomes
from src.data.protocol.database.load_incomes_repository import LoadIncomesRepository

class DbLoadIncomes(LoadIncomes):
    def __init__(self, load_incomes_repository: LoadIncomesRepository) -> None:
        self.repository = load_incomes_repository

    async def load_incomes(self, user_id: str) -> List[Income]:
        return await self.repository.load_incomes(user_id=user_id)