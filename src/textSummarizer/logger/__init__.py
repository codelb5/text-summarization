import os
import sys
import logging
from datetime import datetime
from pathlib import Path


LOGGER_STR = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
LOG_DIR = "logs"
LOG_FILENAME = "running_logs.log"
LOGFILE_PATH = os.path.join(LOG_DIR, LOG_FILENAME)

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=LOGGER_STR,
    handlers=[
        logging.FileHandler(filename=LOGFILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(name="textSummarizerLogger")



