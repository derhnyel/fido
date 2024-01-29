from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from core.security import DEFAULT_SECURITY_HANDLER
from core.exceptions.exceptions import AuthenticationRequiredException



class AuthenticationRequired:
    """
    Authentication required dependency.
    Args:
        token: HTTP Authorization credentials
    Raises:
        AuthenticationRequiredException: If the token is invalid or not provided.
    """

    def __init__(
        self,
        credentials: HTTPBasicCredentials = Depends(HTTPBasic(auto_error=False)),
    ) -> None:
        if not credentials:
            raise AuthenticationRequiredException()
        try:
            DEFAULT_SECURITY_HANDLER.verify(
                credentials=credentials
            )
        except Exception as e:
            raise AuthenticationRequiredException(
                "Invalid token provided for authentication!"
            ) from e
