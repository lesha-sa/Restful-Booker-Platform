from src.db.connector import get_db_connection
from src.models.room_template import RoomTemplate
from typing import List


def get_all_room_templates() -> List[RoomTemplate]:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT room_id, room_number, room_type, accessible, price, additional_services
        FROM room_templates
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [RoomTemplate(*row) for row in rows]
