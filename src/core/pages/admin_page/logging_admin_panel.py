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
        try:
            logger.debug("Starting authorization")
            self.input_login()
            self.input_password()
            self.click_button_login()
            logger.success("Authorization successful")
        except Exception as e:
            logger.error(f"Authorization failed: {e}")
            raise

    def input_login(self):
        self.element_is_visible(self.locators.INPUT_LOGIN_USER_NAME).send_keys('admin')
        logger.debug("Entered login")

    def input_password(self):
        self.element_is_visible(self.locators.INPUT_LOGIN_PASSWORD).send_keys('password')
        logger.debug("Entered password")

    def click_button_login(self):
        self.element_is_visible(self.locators.BUTTON_LOGIN).click()
        logger.debug("Clicked login button")
        time.sleep(1)
