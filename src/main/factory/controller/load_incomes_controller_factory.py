from src.main.factory.usecase.load_incomes_factory import makeLoadIncomes
from src.presentation.controller.load_incomes_controller import LoadIncomesController
from src.presentation.protocol.controller import Controller

def makeLoadIncomesController() -> Controller:
    LoadIncomes = makeLoadIncomes()
    return LoadIncomesController(LoadIncomes)