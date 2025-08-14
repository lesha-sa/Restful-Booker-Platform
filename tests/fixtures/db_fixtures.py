import pytest
from src.db.connector import get_db_connection
from config.logger.config_logger import get_logger

logger = get_logger()


@pytest.fixture(scope='function')
def db_connection():
    """
    Fixture for establishing a connection to the database.
    Returns the connection object and closes it after the test
    """
    logger.debug("Opening DB connection")
    conn = get_db_connection()
    try:
        yield conn
    finally:
        conn.close()
        logger.debug("DB connection closed")
