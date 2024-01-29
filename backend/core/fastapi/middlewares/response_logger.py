from typing import Optional
from pydantic import BaseModel, Field
from starlette.datastructures import Headers
from starlette.types import ASGIApp, Message, Receive, Scope, Send

class ResponseInfo(BaseModel):
    headers: Optional[Headers] = Field(default=None, title="Response header")
    body: str = Field(default="", title="Response body")
    status_code: Optional[int] = Field(default=None, title="Status code")

    class Config:
        """
        Model configuration.
        """

        arbitrary_types_allowed = True


class ResponseLoggerMiddleware:
    """
    Middleware for logging response.
    """

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """
        Log the response.
        """
        if scope["type"] not in ["http"] :
            return await self.app(scope, receive, send)

        response_info = ResponseInfo()

        async def _logging_send(message: Message) -> None:
            """
            Send the response and log it.
            Args:
                message: The message.
            """
            if message.get("type") == "http.response.start":
                response_info.headers = Headers(raw=message.get("headers"))
                response_info.status_code = message.get("status")
            elif message.get("type") == "http.response.body":
                if body := message.get("body"):
                    response_info.body += body.decode("utf8")

            await send(message)

        await self.app(scope, receive, _logging_send)
