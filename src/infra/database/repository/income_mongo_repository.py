from typing import List

from domain.model.income import Income
from data.protocol.database.save_income_repository import SaveIncomeRepository
from data.protocol.database.load_incomes_repository import LoadIncomesRepository
from infra.database.entity.income_entity import IncomeEntity

class IncomeMongoRepository(SaveIncomeRepository, LoadIncomesRepository):
    async def save_income(self, income: Income) -> bool:
        try:
            await IncomeEntity(
                account_id=income.account_id,
                user_id=income.user_id,
                value=income.value,
            ).save()
            return True
        except:
            return False
        
    async def load_incomes(self, user_id: str) -> List[Income]:
        return await IncomeEntity.find({"user_id": user_id}).to_list()