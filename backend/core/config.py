from enum import Enum
import os
from pydantic import BaseSettings #PostgresDsn, RedisDsn
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception as e:
    pass

# EnvironmentType

class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True


class Config(BaseConfig):
    workers: int = 1
    app = "core.server:app"
    log_level: str = "info"
    log_config: str = "logging.conf"
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("APP_PORT", 8000))
    DEBUG: int = 0
    DEFAULT_LOCALE: str = "en_US"
    ENVIRONMENT: str = EnvironmentType.DEVELOPMENT
    RELEASE_VERSION: str = "0.1"
    CORS_ALLOW_ORIGIN: list[str] = ["*"]
    CORS_ALLOW_METHOD: list[str] = ["*"]
    CORS_ALLOW_HEADER: list[str] = ["*"]
    CORS_ALLOW_CREDENTAILS: bool = True
    BASIC_AUTH_USERNAME: str = os.getenv("BASIC_AUTH_USERNAME","admin")
    BASIC_AUTH_PASSWORD: str = os.getenv("BASIC_AUTH_PASSWORD","Admin@1234")
    DEFAULT_SECURITY_HANDLER:str = "basic"


config: Config = Config()
