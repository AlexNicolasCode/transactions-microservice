from domain.model.income import Income
from domain.usecase.save_income import SaveIncome
from data.protocol.database.save_income_repository import SaveIncomeRepository

class DbSaveIncome(SaveIncome):
    def __init__(self, save_income_repository: SaveIncomeRepository) -> None:
        self.repository = save_income_repository

    def save_income(self, income: Income) -> bool:
        return self.repository.save_income(income=income)