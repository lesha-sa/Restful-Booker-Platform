import random
import httpx
from src.api.get_auth_token import get_token
from config.logger.config_logger import get_logger

logger = get_logger()


class TestCreateRoom:
    def test_create_room(self, room_templates_list):
        """
        Creating a room via API.
        Takes a random room template from room_templates and checks that the API returns a 200 status.
        """
        logger.info("=== Start of test: creating a room via API ===")

        # Receive a token
        token = get_token()
        headers = {'Cookie': f'token={token}'}
        logger.info(f"Token received: {token}")

        # Selecting a room template
        room = random.choice(room_templates_list)
        logger.info(f"Room template selected: {room}")

        # Forming the payload
        payload = {
            "roomName": room.room_number,
            "type": room.room_type,
            "accessible": room.accessible,
            "features": room.room_details.split(",") if room.room_details else [],
            "roomPrice": int(room.price)
        }
        logger.info(f"Payload for the request: {payload}")

        # Send a POST request
        response = httpx.post(
            'https://automationintesting.online/api/room',
            headers=headers,
            json=payload,
        )
        logger.info(f"Response: {response.status_code}, {response.text}")

        # Checking the result
        assert response.status_code == 200, (
            f"Status 200 was expected, but received {response.status_code}: {response.text}"
        )
        logger.success("Test passed: room successfully created via API")
