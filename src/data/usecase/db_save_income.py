from src.domain.model.income import Income
from src.domain.usecase.save_income import SaveIncome
from src.data.protocol.database.save_income_repository import SaveIncomeRepository

class DbSaveIncome(SaveIncome):
    def __init__(self, save_income_repository: SaveIncomeRepository) -> None:
        self.repository = save_income_repository

    async def save_income(self, income: Income) -> bool:
        return await self.repository.save_income(income=income)