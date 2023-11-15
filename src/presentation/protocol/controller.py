from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic

from presentation.protocol.http import HttpResponse
from presentation.protocol.http import HttpRequest

R = TypeVar("R")

class Controller(metaclass=ABCMeta):
    
    @abstractmethod
    async def handle(self, request: HttpRequest) -> HttpResponse[R]:
        pass