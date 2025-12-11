import logging
import os
from logging.handlers import TimedRotatingFileHandler

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE_PATH = os.path.join(LOG_DIR, "app.log")

LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT)

time_handler = TimedRotatingFileHandler(
    filename=LOG_FILE_PATH,
    when="midnight",  # rotate at midnight
    interval=1,  # every 1 day
    backupCount=7,  # keep 7 days of logs
    utc=False  # set True if you want UTC time instead of local time
)
time_handler.suffix = "%Y-%m-%d"  # log file name format: app.log.2025-12-11
time_handler.extMatch = r"^\d{4}-\d{2}-\d{2}$"
time_handler.setLevel(LOGGING_LEVEL)
time_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))

_logger = logging.getLogger("uvicorn")

_logger.addHandler(time_handler)

_logger.info("server started running")

logger = _logger
