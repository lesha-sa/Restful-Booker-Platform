import os
from loguru import logger

logger.remove()  # remove logging from console

log_dir = os.path.join(os.path.dirname(__file__),'..','..','logs', 'logs.log')
logger.add(log_dir,
           rotation='10 MB',
           mode='w',
           level='DEBUG')

def get_logger():
    return logger


