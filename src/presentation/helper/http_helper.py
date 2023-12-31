from typing import TypeVar

from src.presentation.protocol.http import HttpResponse

T = TypeVar("T")

def ok (body: T) -> HttpResponse[T]:
    return {
        "status_code": 200,
        "body": body
    }

def created () -> HttpResponse[None]:
    return {
        "status_code": 201,
        "body": None
    }

def serverError () -> HttpResponse[None]:
    return {
        "status_code": 500,
        "body": None
    }