from fastapi import APIRouter

from app.schemas.extras.health import Health
from core.config import config

health_router = APIRouter()


@health_router.get("/")
async def health() -> Health:
    # IMPROVE: Add database health check
    # IMPROVE: Add cache health check
    # IMPROVE: Add other health checks
    # IMPROVE: Add logging health check
    # IMPROVE: Add other health checks
    return Health(version=config.RELEASE_VERSION, status="Healthy")
