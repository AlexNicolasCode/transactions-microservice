from abc import ABCMeta, abstractmethod
from typing import TypeVar

from src.presentation.protocol.http import HttpResponse
from src.presentation.protocol.http import HttpRequest

R = TypeVar("R")

class Controller(metaclass=ABCMeta):
    
    @abstractmethod
    async def handle(self, request: HttpRequest) -> HttpResponse[R]:
        pass