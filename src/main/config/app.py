from fastapi import FastAPI, Response
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from src.infra.database.entity.income_entity import IncomeEntity
from src.main.route.income_routes import income_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient("mongodb://test:test@localhost:27017")
    await init_beanie(database=client.db_name, document_models=[IncomeEntity])
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(income_router)

@app.get("/")
async def root() -> None:
    return Response(status_code=404)

