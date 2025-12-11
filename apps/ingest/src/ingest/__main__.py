"""Server module for the application."""

from fastapi import FastAPI
import inngest.fast_api

from core.workflows.client import inngest_client
from core.workflows.workflow_hello_world import hello_world
from core.workflows.workflow_sync_systems import sync_systems

app = FastAPI()

inngest.fast_api.serve(app, inngest_client, [
    hello_world,
    sync_systems
])
