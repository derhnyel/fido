from fastapi import APIRouter, Depends
from .monitoring import monitoring_router
from .generator import password_router
from core.fastapi.dependencies import AuthenticationRequired

# Routes
v1_router = APIRouter()
v1_router.include_router(monitoring_router, prefix="/monitoring", dependencies=[Depends(AuthenticationRequired)])
v1_router.include_router(password_router, prefix="") #dependencies=[Depends(AuthenticationRequired)])

