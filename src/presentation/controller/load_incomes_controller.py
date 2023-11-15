from typing import List

from src.presentation.protocol.controller import Controller
from src.presentation.protocol.http import HttpResponse, HttpRequest
from src.presentation.helper.http_helper import ok
from src.domain.usecase.load_incomes import LoadIncomes

class LoadIncomesController(Controller):

    def __init__(self, load_incomes_external: LoadIncomes):
        self.load_incomes = load_incomes_external

    async def handle(self, request: HttpRequest) -> HttpResponse:
        incomes = await self.load_incomes.load_incomes(request.body["user_id"])
        return ok(incomes)