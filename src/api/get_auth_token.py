import httpx
from config.logger.config_logger import get_logger

logger = get_logger()


AUTH_URL = "https://automationintesting.online/api/auth/login"
AUTH_PAYLOAD = {
    "username": "admin",
    "password": "password"
}
TIMEOUT = 10.0

def get_token() -> str:
    """Receives an authorization token from the server."""
    try:
        response = httpx.post(
            AUTH_URL,
            json = AUTH_PAYLOAD,
            timeout=TIMEOUT
        )
        response.raise_for_status()
        token = response.json().get("token")
        assert token, "Token not found in response"
        logger.info("Token successfully received")
        return token
    except Exception as e:
        logger.error("Unable to obtain token: {}", e)
        raise