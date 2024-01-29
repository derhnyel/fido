from api import router
from typing import List
from fastapi import Depends, FastAPI,Request
from core.config import config
from fastapi.responses import JSONResponse
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from core.fastapi.middlewares import (
    BasicAuthBackend,
    AuthenticationMiddleware,
    ResponseLoggerMiddleware,
)
from core.fastapi.dependencies import Logging
from core.exceptions import CustomException


def init_routers(app_: FastAPI) -> None:
    """
    Adds the routers to the FastAPI application.
    Args:
        app_: The FastAPI application.
    """

    app_.include_router(router)


def make_middleware() -> List[Middleware]:
    """
    Makes the middleware for the FastAPI application.
    Returns:
        List[Middleware]: The list of middleware.
    """
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=config.CORS_ALLOW_ORIGIN,
            allow_credentials=config.CORS_ALLOW_CREDENTAILS,
            allow_methods=config.CORS_ALLOW_METHOD,
            allow_headers=config.CORS_ALLOW_HEADER,
        ),
        Middleware(
            AuthenticationMiddleware,
            backend=BasicAuthBackend(),
            on_error=on_auth_error,
        ),
        Middleware(ResponseLoggerMiddleware),
    ]
    return middleware


def init_listeners(app_: FastAPI) -> JSONResponse:
    """
    Adds the listener exception handler to the FastAPI application.
    Args:
        app_: The FastAPI application.
    Returns:
        JSONResponse: The JSON response.
    """

    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )

def on_auth_error(request: Request, exc: Exception) -> JSONResponse:
    """
    Authentication error handler.
    Args:
        request: The request object.
        exc: The exception object.
    Returns:
        JSONResponse: The JSON response.
    """
    status_code, error_code, message = 401, None, str(exc)
    if isinstance(exc, CustomException):
        status_code = int(exc.code)
        error_code = exc.error_code
        message = exc.message

    return JSONResponse(
        status_code=status_code,
        content={"error_code": error_code, "message": message},
    )


def create_app() -> FastAPI:
    """
    Creates the FastAPI application with all the required configurations, middlewares, routers, listeners, etc.
    """
    app_ = FastAPI(
        title="Fido Test API",
        description="Coding challenge for fido",
        version=config.RELEASE_VERSION,
        docs_url=None
        if config.ENVIRONMENT == "production"
        else "/docs",  # Swagger UI is disabled in production
        redoc_url=None
        if config.ENVIRONMENT == "production"
        else "/redoc",  # ReDoc is disabled in production
        dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    init_listeners(app_=app_)
    return app_


app = create_app()