import httpx

def get_token():
    response = httpx.post(
        'https://automationintesting.online/api/auth/login',
        json={"username": "admin", "password": "password"}
    )
    assert response.status_code == 200
    return response.json()["token"]