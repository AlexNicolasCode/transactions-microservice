from src.main.factory.usecase.save_income_factory import makeSaveIncome
from src.presentation.controller.save_income_controller import SaveIncomeController
from src.presentation.protocol.controller import Controller

def makeSaveIncomeController() -> Controller:
    saveIncome = makeSaveIncome()
    return SaveIncomeController(saveIncome)