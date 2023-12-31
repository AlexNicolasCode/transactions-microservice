from abc import ABCMeta, abstractmethod

from src.domain.model.income import Income

class SaveIncome(metaclass=ABCMeta):
    @abstractmethod
    async def save_income(self, income: Income) -> bool:
        pass