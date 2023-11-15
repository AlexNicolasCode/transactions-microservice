import jwt
from fastapi import APIRouter, Response, Depends
from fastapi.security import OAuth2PasswordBearer

from domain.dto.save_income_dto import SaveIncomeDTO
from domain.dto.load_incomes_dto import LoadIncomesDTO
from presentation.protocol.http import HttpRequest
from main.factory.controller.save_income_controller_factory import makeSaveIncomeController
from main.factory.controller.load_incomes_controller_factory import makeLoadIncomesController

income_router = APIRouter(
    prefix="/income"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@income_router.get("/")
async def load(token: str = Depends(oauth2_scheme)) -> list:
    decoded_token = jwt.decode(token, options={"verify_signature": False})
    request = HttpRequest[LoadIncomesDTO]()
    request.body = {"user_id": decoded_token["user_id"]}
    controller = makeLoadIncomesController()
    response = await controller.handle(request)
    if response["status_code"] == 200:
        return response["body"]
    return Response(status_code = 500)

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