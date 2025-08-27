import allure
from src.api.get_auth_token import get_token

@allure.feature("Authorization")
@allure.story("Get API token")
def test_auth():
    """
    Checking token authorization via API.
    The test verifies that the get_token function returns a valid token.
    """

    with allure.step("Get token via API helper"):
        token = get_token()
        allure.attach(token, name="Received Token", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Check that token is not None"):
        assert token is not None, "The token was not received."

