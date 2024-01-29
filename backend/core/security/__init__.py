from .basic import BasicAuthHandler,PasswordHandler
from core.config import config
SecurityHandler:dict = {
    "basic":BasicAuthHandler
    }
DEFAULT_SECURITY_HANDLER = SecurityHandler[config.DEFAULT_SECURITY_HANDLER.lower()]
__all__ = [
    "PasswordHandler", DEFAULT_SECURITY_HANDLER
]

