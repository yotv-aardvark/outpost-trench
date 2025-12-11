import logging
from datetime import UTC, datetime

from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from app.schema.status_check import HealthCheck

router = APIRouter(tags=["health"])

STATUS_HEALTHY = "healthy"
STATUS_UNHEALTHY = "unhealthy"

LOGGER = logging.getLogger(__name__)


@router.get("/health", response_model=HealthCheck)
async def health():
    http_status = status.HTTP_200_OK
    response = {
        "status": STATUS_HEALTHY,
        "environment": "env",
        # "environment": settings.ENVIRONMENT.value,
        "version": "v1.0.1",
        # "version": settings.APP_VERSION,
        "timestamp": datetime.now(UTC).isoformat(timespec="seconds"),
        # "timestamp": datetime.now(UTC).isoformat(timespec="seconds"),
    }

    return JSONResponse(status_code=http_status, content=response)
