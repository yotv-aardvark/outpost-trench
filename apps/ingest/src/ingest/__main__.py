"""Server module for the application."""

from fastapi import FastAPI
import inngest.fast_api
from starlette.responses import RedirectResponse

from core.logger.logger import logger
from core.workflows.client import inngest_client
from core.workflows.workflow_hello_world import hello_world
from core.workflows.workflow_sync_systems import sync_systems
from ingest.api import api_router

app = FastAPI(
    title="Ingest API",
    version="1.0.0",
    description="Ingest API",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(api_router)
logger.info("api registered routes")


@app.get("/", include_in_schema=False)
def redirect_to_docs():
    """Redirect to the API documentation."""
    logger.info("Redirecting to /docs")
    return RedirectResponse(url="/docs")


inngest.fast_api.serve(app, inngest_client, [
    hello_world,
    sync_systems
])
