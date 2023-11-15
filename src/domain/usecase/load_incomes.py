from typing import List
from abc import ABCMeta, abstractmethod

from src.domain.model.income import Income

class LoadIncomes(metaclass=ABCMeta):
    @abstractmethod
    async def load_incomes(self, user_id: str) -> List[Income]:
        pass