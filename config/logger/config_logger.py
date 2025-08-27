import os
from pathlib import Path
from loguru import logger

logger.remove()  # Remove the standard output to the console

env_log_path = os.getenv("LOG_PATH")  # Attempt to obtain from the environment

if env_log_path:
    log_dir = Path(env_log_path)
else:
    # Default local path for logs ./logs in the project root
    log_dir = Path(__file__).resolve().parent.parent.parent / "logs"

log_dir.mkdir(parents=True, exist_ok=True)  # Create a folder if it does not exist

log_file = log_dir / "logs.log"

logger.add(
    log_file,
    rotation='10 MB',
    mode='w',
    level='DEBUG',
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{line} | {message}"

)

def get_logger():
    return logger
