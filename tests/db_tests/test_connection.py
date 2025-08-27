import pytest
import allure
from config.logger.config_logger import get_logger
from src.db.connector import get_db_connection

logger = get_logger()


def is_db_available():
    """
    Checks whether the database is accessible via get_db_connection.
    """
    try:
        conn = get_db_connection()
        conn.close()
        return True
    except Exception:
        return False


@pytest.mark.skipif(not is_db_available(), reason="Database unavailable")
@allure.feature("Database")
@allure.story("Check public tables")
def test_simple_db_query(db_connection):
    """
    Checking for tables in the database.
    The test performs a simple query to information_schema.tables and verifies
    that at least one table exists.
    """
    logger.info("=== Start of test: checking for tables in the database ===")

    with allure.step("Query public tables from information_schema"):
        cursor = db_connection.cursor()
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """)
        tables = cursor.fetchall()
        cursor.close()

    allure.attach(str([t[0] for t in tables]), name="Tables Found", attachment_type=allure.attachment_type.TEXT)
    logger.info(f"Tables found: {len(tables)}")

    with allure.step("Verify at least one table exists"):
        assert len(tables) > 0, "No tables found in the database"
        logger.success("Test passed: tables found in the database")
