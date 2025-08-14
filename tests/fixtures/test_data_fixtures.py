import json
import os
import pytest

from src.db.connector import get_db_connection
from src.repository.room_template_repository import get_all_room_templates
from src.schemas.room_template import RoomTemplate
from config.logger.config_logger import get_logger

logger = get_logger()


@pytest.fixture(scope="function")
def room_templates_list():
    """
    Returns a list of RoomTemplate objects.
    Takes data from the database if the connection is available.
    If the database is unavailable, uses a JSON file
    """
    try:
        conn = get_db_connection()
        conn.close()
        # If the connection is successful, we retrieve data from the database
        return get_all_room_templates()
    except Exception as e:
        logger.warning(f"DB unavailable, loading room templates from JSON. Exception: {e}")
        # If the database is unavailable, read JSON
        json_path = os.path.join(os.path.dirname(__file__), "..", "..", "src", "test_data", "room_templates.json")
        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)
        return [RoomTemplate(**item) for item in data]
