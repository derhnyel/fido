from app.controllers import PasswordGeneratorController
from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.responses import JSONResponse
from app.schemas.responses.password import Password
from app.schemas.requests.password  import  RequestPassword

# PasswordRouter
password_router = APIRouter()


@password_router.post("/generate-password")
async def get_device(
    request_password: RequestPassword,
    generator: Annotated[None, Depends(PasswordGeneratorController())]
) -> JSONResponse:
    """
    Generates a password randomly.
    """
    return Password(password=await generator(
        length=request_password.length,
        special_characters_allowed=request_password.special_characters,
        digits_allowed=request_password.digits,
        uppercase_allowed=request_password.uppercase,
        lowercase_allowed=request_password.lowercase,
        startswith=request_password.startswith,
        endswith=request_password.endswith,
        must_contain=request_password.must_contain,
        not_startswith=request_password.not_startswith,
        not_endswith=request_password.not_endswith,
        must_not_contain=request_password.must_not_contain
    ))