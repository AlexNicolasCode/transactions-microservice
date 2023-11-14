from main.factory.usecase.save_income_factory import makeSaveIncome
from presentation.controller.save_income_controller import SaveIncomeController
from presentation.protocol.controller import Controller

def makeSaveIncomeController() -> Controller:
    saveIncome = makeSaveIncome()
    return SaveIncomeController(saveIncome)