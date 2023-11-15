from typing import TypeVar

import jwt
from fastapi import Response

from src.presentation.protocol.http import HttpRequest
from src.presentation.protocol.controller import Controller

T = TypeVar("T")

async def route_adapter(controller: Controller, body: T, token: str) -> Response:
    request = HttpRequest()
    request.body = body
    if token != None:
        decoded_token = jwt.decode(token, options={"verify_signature": False})
        request.body["user_id"] = decoded_token["user_id"]
    response = await controller.handle(request)
    status_mapper = {
        200: response["body"],
        201: None,
        500: Response(status_code=500),
    }
    return status_mapper.get(response["status_code"], 500)