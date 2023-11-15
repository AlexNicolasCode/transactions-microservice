from fastapi import APIRouter, Response

from domain.dto.save_income_dto import SaveIncomeDTO
from presentation.protocol.http import HttpRequest
from main.factory.controller.save_income_controller_factory import makeSaveIncomeController

income_router = APIRouter(
    prefix="/income"
)

@income_router.post("/")
async def save(income: SaveIncomeDTO) -> None:
    request = HttpRequest[SaveIncomeDTO]()
    request.body = income
    controller = makeSaveIncomeController()
    response = await controller.handle(request)
    return Response(
        status_code=response["status_code"],
        content=response["body"],
    )