from src.db.connector import get_db_connection
from src.schemas.room_template import RoomTemplate
from typing import List

def get_all_room_templates() -> List[RoomTemplate]:
    """
    Retrieves all room templates from the database.
    Returns a list of RoomTemplate objects
    """
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT room_id, room_number, room_type, accessible, price, room_details
                FROM room_templates
            """)
            rows = cursor.fetchall()

    return [RoomTemplate(*row) for row in rows]
