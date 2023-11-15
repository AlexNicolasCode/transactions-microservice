from typing import List
from abc import ABCMeta, abstractmethod

from src.domain.model.income import Income

class LoadIncomesRepository(metaclass=ABCMeta):
    @abstractmethod
    def save_income(self, user_id: str) -> List[Income]:
        pass