import random
import httpx
import allure
from src.api.get_auth_token import get_token
from config.logger.config_logger import get_logger

logger = get_logger()


@allure.feature("Room management")
class TestCreateRoom:

    @allure.story("Create a room via API")
    def test_create_room(self, room_templates_list):
        """
        Creating a room via API.
        Takes a random room template from room_templates and checks that the API returns a 200 status.
        """
        logger.info("=== Start of test: creating a room via API ===")

        with allure.step("Get auth token"):
            token = get_token()
            headers = {'Cookie': f'token={token}'}
            logger.info(f"Token received: {token}")
            allure.attach(token, name="Auth Token", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Select random room template"):
            room = random.choice(room_templates_list)
            logger.info(f"Room template selected: {room}")
            allure.attach(str(room), name="Selected Room Template", attachment_type=allure.attachment_type.TEXT)


        with allure.step("Prepare payload"):
            payload = {
                "roomName": room.room_number,
                "type": room.room_type,
                "accessible": room.accessible,
                "features": room.room_details.split(",") if room.room_details else [],
                "roomPrice": int(room.price)
            }
            logger.info(f"Payload for the request: {payload}")
            allure.attach(str(payload), name="Payload", attachment_type=allure.attachment_type.JSON)

        with allure.step("Send POST request to create room"):
            response = httpx.post(
                'https://automationintesting.online/api/room',
                headers=headers,
                json=payload,
            )
            logger.info(f"Response: {response.status_code}, {response.text}")
            allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Check response status"):
            assert response.status_code == 200, (
                f"Status 200 was expected, but received {response.status_code}: {response.text}"
            )
            logger.success("Test passed: room successfully created via API")
