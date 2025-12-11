import logging

import inngest

inngest_client = inngest.Inngest(
    app_id="ingest_server_runner",
    logger=logging.getLogger("uvicorn"),
)
