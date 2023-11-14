from domain.model.income import Income
from data.protocol.database.save_income_repository import SaveIncomeRepository
from infra.database.entity.income_entity import IncomeEntity

class IncomeMongoRepository(SaveIncomeRepository):
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