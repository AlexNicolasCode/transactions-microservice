from main.factory.usecase.load_incomes_factory import makeLoadIncomes
from presentation.controller.load_incomes_controller import LoadIncomesController
from presentation.protocol.controller import Controller

def makeLoadIncomesController() -> Controller:
    LoadIncomes = makeLoadIncomes()
    return LoadIncomesController(LoadIncomes)