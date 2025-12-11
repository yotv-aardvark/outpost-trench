import inngest

from core.logger.logger import logger

inngest_client = inngest.Inngest(
    app_id="ingest_server_runner",
    logger=logger,
)
