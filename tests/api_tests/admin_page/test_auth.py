from src.api.get_auth_token import get_token


def test_auth():
    """
    Checking token authorization via API.
    The test verifies that the get_token function returns a valid token.
    """

    token = get_token()

    assert token is not None, "The token was not received."

