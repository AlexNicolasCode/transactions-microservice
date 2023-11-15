import jwt
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from src.domain.dto.save_income_dto import SaveIncomeDTO
from src.main.factory.controller.save_income_controller_factory import makeSaveIncomeController
from src.main.factory.controller.load_incomes_controller_factory import makeLoadIncomesController
from src.main.adapter.route_adapter import route_adapter

income_router = APIRouter(
    prefix="/income"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@income_router.get("/")
async def load(token: str = Depends(oauth2_scheme)) -> list:
    return await route_adapter(makeLoadIncomesController(), {}, token)

@income_router.post("/")
async def save(income: SaveIncomeDTO) -> None:
    return await route_adapter(makeSaveIncomeController(), income, None)