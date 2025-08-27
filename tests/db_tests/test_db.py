import pytest
import allure
from config.logger.config_logger import get_logger
from src.repository.room_template_repository import get_all_room_templates
from src.db.connector import get_db_connection

logger = get_logger()


def is_db_available():
    """
    Checks whether the database is accessible via get_db_connection
    """
    try:
        conn = get_db_connection()
        conn.close()
        return True
    except Exception:
        return False


@pytest.mark.skipif(not is_db_available(), reason="Database unavailable")
@allure.feature("Room templates")
@allure.story("Check room template data")
def test_all_data():
    """
    Checking of room template data
    The test is performed only if the database is available
    """
    with allure.step("Get all room templates"):
        data = get_all_room_templates()

    with allure.step("Verify that data exists"):
        assert len(data) > 0, "The list of room templates is empty"
        logger.info(f"Room templates found: {len(data)}")
        allure.attach(str([t.room_number for t in data]), name="Room templates", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Check first template"):
        first = data[0]
        assert first.price is not None, "The price for the first template is not specified"
        assert hasattr(first, "room_number"), "The first template does not have a room number"
        logger.info(f"First template: {first.room_number}, цена: {first.price}")

    if len(data) > 1:
        with allure.step("Check second template"):
            second = data[1]
            assert second.price is not None, "The price for the second template is not specified"
            logger.info(f"Second template: {second.room_number}, price: {second.price}")
