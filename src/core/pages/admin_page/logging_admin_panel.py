import time

from config.logger.config_logger import get_logger

from src.core.locators.admin_page.locators import AdminPageLocators
from src.core.pages.base_page import BasePage

logger = get_logger()


def enter_login_name(user_name_field, param):
    pass


class AdminPageLogging(BasePage):
    locators = AdminPageLocators

    def admin_page_loging(self):
        """admin panel login"""
        # enter_login_name(user_name_field, 'admin')
        # enter_login_password()
        try:
            logger.debug("Beginning of authorization")
            self.input_login()
            self.input_password()
            self.click_button_login()
            logger.success("Successful authorization")
        except Exception as e:
            logger.error(f"Authorization error: {str(e)}")
            raise

    def input_login(self):
        self.element_is_visible(self.locators.INPUT_LOGIN_USER_NAME).send_keys('admin')

    def input_password(self):
        self.element_is_visible(self.locators.INPUT_LOGIN_PASSWORD).send_keys('password')

    def click_button_login(self):
        self.element_is_visible(self.locators.BUTTON_LOGIN).click()
        time.sleep(1)
