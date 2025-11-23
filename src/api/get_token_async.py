import httpx
from config.logger.config_logger import get_logger

logger = get_logger()

AUTH_URL = "https://automationintesting.online/api/auth/login"
AUTH_PAYLOAD = {
    "username": "admin",
    "password": "password"
}
TIMEOUT = 10.0


async def get_token_async() -> str:
    """Asynchronously receives an authorization token from the server."""
    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await client.post(
                AUTH_URL,
                json=AUTH_PAYLOAD
            )
            response.raise_for_status()

        token = response.json().get("token")
        assert token, "Token not found in response"

        logger.info("Token successfully received (async)")
        return token

    except Exception as e:
        logger.error(f"Unable to obtain token (async): {e}")
        raise
