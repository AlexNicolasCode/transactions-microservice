from src.domain.usecase.save_income import SaveIncome
from src.data.usecase.db_save_income import DbSaveIncome
from src.infra.database.repository.income_mongo_repository import IncomeMongoRepository

def makeSaveIncome() -> SaveIncome:
    repository = IncomeMongoRepository()
    return DbSaveIncome(repository)