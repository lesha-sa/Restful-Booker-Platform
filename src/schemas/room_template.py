from dataclasses import dataclass
from typing import Optional

@dataclass
class RoomTemplate:
    """
    Data class for storing room template information.
    """
    room_id: int
    room_number: str
    room_type: str
    accessible: bool
    price: float
    room_details: Optional[str]
