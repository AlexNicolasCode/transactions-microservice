from abc import ABCMeta, abstractmethod

from src.domain.model.income import Income

class SaveIncomeRepository(metaclass=ABCMeta):
    @abstractmethod
    def save_income(self, income: Income) -> bool:
        pass