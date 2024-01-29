import secrets

from fastapi.security import HTTPBasicCredentials
from core.config import config
from core.exceptions import UnauthorizedException

from passlib.context import CryptContext


class PasswordHandler:
    """
    PasswordHandler class to hash and verify passwords.
    """
    pwd_context = CryptContext(
        schemes=["bcrypt"],
        deprecated="auto",
    )

    @staticmethod
    def hash(password: str):
        return PasswordHandler.pwd_context.hash(password)

    @staticmethod
    def verify(hashed_password, plain_password):
        return PasswordHandler.pwd_context.verify(plain_password, hashed_password)

class BasicAuthHandler:
    """
    Basic Auth Handler Class
    """
    _username = config.BASIC_AUTH_USERNAME  
    _password = config.BASIC_AUTH_PASSWORD
    busername = _username.encode("utf8")
    bpassword = _password.encode("utf8")

    def __init__(self,username=None,password=None):
        if username:
            self._username = username
            self.busername = self._username.encode("utf8")
        if password:
            self._password = password
            self.bpassword = self._password.encode("utf8")
    
    @classmethod
    def set_credentials(cls,username,password):
        cls._username = username
        cls._password = password
        cls.busername = cls._username.encode("utf8")
        cls.bpassword = cls._password.encode("utf8")

    @staticmethod
    def verify(credentials: HTTPBasicCredentials) -> bool:
        """
        Verify the credentials
        Args:
            credentials: HTTPBasicCredentials
        Returns:
            True if the credentials are valid, False otherwise
        Raises:
            UnauthorizedException: If the credentials are not valid
        """
        if not (credentials.username and credentials.password):
            raise UnauthorizedException()
        current_username_bytes = credentials.username.encode("utf8")
        is_correct_username = secrets.compare_digest(
            current_username_bytes, BasicAuthHandler.busername
        )
        current_password_bytes = credentials.password.encode("utf8")
        is_correct_password = secrets.compare_digest(
            current_password_bytes, BasicAuthHandler.bpassword
        )
        if not (is_correct_username and is_correct_password):
            raise UnauthorizedException()
        return True