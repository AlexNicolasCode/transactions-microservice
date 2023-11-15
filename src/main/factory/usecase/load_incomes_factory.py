from domain.usecase.load_incomes import LoadIncomes
from data.usecase.db_load_incomes import DbLoadIncomes
from infra.database.repository.income_mongo_repository import IncomeMongoRepository

def makeLoadIncomes() -> LoadIncomes:
    repository = IncomeMongoRepository()
    return DbLoadIncomes(repository)