from abc import ABCMeta, abstractmethod

from domain.model.income import Income

class SaveIncome(metaclass=ABCMeta):
    @abstractmethod
    def save_income(self, income: Income) -> bool:
        pass