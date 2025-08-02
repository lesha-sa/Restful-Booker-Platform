from src.api.get_auth_token import get_token


def test_auth():
    token = get_token()
    print("Token:", token)
    assert token is not None
