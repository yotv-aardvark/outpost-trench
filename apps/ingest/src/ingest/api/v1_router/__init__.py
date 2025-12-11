from fastapi import APIRouter
from .status_check import router as status_check_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(status_check_router)
