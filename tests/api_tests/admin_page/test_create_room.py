import httpx
from src.api.get_auth_token import get_token

class TestCreateRoom:

    def test_create_room(self):
        token = get_token()
        headers = {'Cookie': f'token={token}'}
        response = httpx.post(
            'https://automationintesting.online/api/room',
            headers=headers,
            json={
                "roomName": "1412",
                "type": "Double",
                "accessible": True,
                "features": ["TV", "Safe"],
                "roomPrice": 150
            },
        )
        print("Response:", response.status_code, response.text)
        assert response.status_code == 200
