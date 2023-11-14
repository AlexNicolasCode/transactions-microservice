from presentation.protocol.http import HttpResponse

def created () -> HttpResponse[None]:
    return {
        "status_code": 201,
        "body": None
    }