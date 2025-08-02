from dataclasses import dataclass
from typing import Optional

@dataclass
class RoomTemplate:
    room_id: int
    room_number: str
    room_type: str
    accessible: bool
    price: float
    additional_services: Optional[str]
