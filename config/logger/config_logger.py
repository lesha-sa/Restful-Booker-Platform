import os
from pathlib import Path
from loguru import logger

logger.remove()  # remove logging from console

log_dir = Path(os.getenv("LOG_PATH", Path(__file__).resolve().parent.parent.parent / "logs"))
log_dir.mkdir(parents=True, exist_ok=True)

log_file = log_dir / "logs.log"
logger.add(log_file,
           rotation='10 MB',
           mode='w',
           level='DEBUG')

def get_logger():
    return logger


