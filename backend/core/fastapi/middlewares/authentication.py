from typing import Optional, Tuple
from starlette.responses import PlainTextResponse, Response
from starlette.authentication import AuthenticationBackend
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.requests import HTTPConnection
from core.security import DEFAULT_SECURITY_HANDLER
from pydantic import BaseModel, Field
import base64
from uuid import uuid1

class CurrentUser(BaseModel):
    session_id: str = Field(None, description="Session ID")

    class Config:
        validate_assignment = True



class BasicAuthBackend(AuthenticationBackend):
    """
    Authentication backend. Inherits from starlette.authentication.AuthenticationBackend.
    """

    async def authenticate(
        self, conn: HTTPConnection
    ) -> Tuple[bool, Optional[CurrentUser]]:
        """
        Authenticate the user.
        Args:
            conn: The HTTP connection.
        Returns:
            Tuple: The authentication result (True | Falsd) and the current user.
        Raises:
            AuthenticationError: If the token is invalid or not provided.
            ValueError: If the token is invalid or not provided.
        """
        current_user = CurrentUser()
        conn_type = conn.scope.get("type")

        if "http" in conn_type:
            authorization = conn.headers.get("Authorization")
        if not authorization:
            return False, current_user
        try:
            if "http" in conn_type:
                scheme, credentials = authorization.split(" ")
                if scheme.lower() != "basic":
                    return False, current_user
        except ValueError:
            return False, current_user
        if not credentials:
            return False, current_user
        try:
            decoded_credentials = base64.b64decode(credentials).decode("utf-8")
            username, password = decoded_credentials.split(":")
            cred  = lambda x: x
            cred.username = username
            cred.password = password
            DEFAULT_SECURITY_HANDLER.verify(
                credentials=cred
            )
            
        except Exception as e:
            return False, current_user
        unique_id = str(uuid1())

        current_user.session_id = unique_id
        return True, current_user

    @staticmethod
    def on_error(conn: HTTPConnection, exc: Exception) -> Response:
        """
        Handle authentication error.
        Args:
            conn: The HTTP connection.
            exc: The exception.
        Returns:
            Response: The response. (400) Bad Request.
        """
        return PlainTextResponse(str(exc), status_code=400)
