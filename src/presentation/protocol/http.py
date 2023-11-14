from typing import TypeVar, Generic

T = TypeVar("T")

class HttpResponse(Generic[T]):
    status_code: int
    body: T

class HttpRequest(Generic[T]):
    body: T