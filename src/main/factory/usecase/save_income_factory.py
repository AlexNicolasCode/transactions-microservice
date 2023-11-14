from domain.usecase.save_income import SaveIncome
from data.usecase.db_save_income import DbSaveIncome
from infra.database.repository.income_mongo_repository import IncomeMongoRepository

def makeSaveIncome() -> SaveIncome:
    repository = IncomeMongoRepository()
    return DbSaveIncome(repository)