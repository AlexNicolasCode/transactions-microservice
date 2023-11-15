from presentation.protocol.controller import Controller
from presentation.protocol.http import HttpResponse, HttpRequest
from presentation.helper.http_helper import created, serverError
from domain.usecase.save_income import SaveIncome
from domain.dto.save_income_dto import SaveIncomeDTO

class SaveIncomeController(Controller):

    def __init__(self, save_income_external: SaveIncome):
        self.save_income = save_income_external

    async def handle(self, request: HttpRequest[SaveIncomeDTO]) -> HttpResponse[bool]:
        hasSaved = await self.save_income.save_income(request.body)
        if hasSaved:
            return created()
        else:
            return serverError()