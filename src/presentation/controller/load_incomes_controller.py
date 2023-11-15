from typing import List

from presentation.protocol.controller import Controller
from presentation.protocol.http import HttpResponse, HttpRequest
from presentation.helper.http_helper import ok
from domain.usecase.load_incomes import LoadIncomes
from domain.dto.load_incomes_dto import LoadIncomesDTO
from domain.model.income import Income

class LoadIncomesController(Controller):

    def __init__(self, load_incomes_external: LoadIncomes):
        self.load_incomes = load_incomes_external

    async def handle(self, request: HttpRequest[LoadIncomesDTO]) -> HttpResponse[List[Income]]:
        incomes = await self.load_incomes.load_incomes(request.body)
        return ok[List[Income]](incomes)