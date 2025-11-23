import random
import asyncio
import pytest
import httpx
import allure

from src.api.get_token_async import get_token_async
from config.logger.config_logger import get_logger

logger = get_logger()


@pytest.mark.asyncio
#@pytest.mark.async_api
@allure.feature("Room management")
class TestCreateMultipleRoomsAsync:

    @allure.story("Create multiple rooms via API (async) with Allure attachments")
    async def test_create_multiple_rooms_async(self, room_templates_list):
        logger.info("=== Start async test: creating multiple rooms via API ===")

        with allure.step("Get auth token"):
            token = await get_token_async()
            headers = {'Cookie': f'token={token}'}
            logger.info(f"Token received: {token}")
            allure.attach(token, name="Auth Token", attachment_type=allure.attachment_type.TEXT)

        async def create_room(room):
            payload = {
                "roomName": room.room_number,
                "type": room.room_type,
                "accessible": room.accessible,
                "features": room.room_details.split(",") if room.room_details else [],
                "roomPrice": int(room.price)
            }
            logger.info(f"Payload for room {room.room_number}: {payload}")
            allure.attach(str(payload), name=f"Payload {room.room_number}", attachment_type=allure.attachment_type.JSON)

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    'https://automationintesting.online/api/room',
                    headers=headers,
                    json=payload,
                )

            logger.info(f"Response for room {room.room_number}: {response.status_code}, {response.text}")
            allure.attach(response.text, name=f"Response {room.room_number}", attachment_type=allure.attachment_type.JSON)

            assert response.status_code == 200
            logger.success(f"Room {room.room_number} successfully created")
            return response

        rooms_to_create = [random.choice(room_templates_list) for _ in range(3)]
        results = await asyncio.gather(*(create_room(room) for room in rooms_to_create))

        logger.info(f"{len(results)} rooms created successfully")
