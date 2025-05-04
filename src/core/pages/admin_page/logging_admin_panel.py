import time
import random

from src.core.locators.admin_page.locators import AdminPageLocators
from src.core.pages.base_page import BasePage


def enter_login_name(user_name_field, param):
    pass


class AdminPageLogging(BasePage):
    locators = AdminPageLocators

    def admin_page_loging(self):
        #enter_login_name(user_name_field, 'admin')
        #enter_login_password()
        self.element_is_visible(self.locators.INPUT_LOGIN_USER_NAME).send_keys('admin')
        time.sleep(1)
        self.element_is_visible(self.locators.INPUT_LOGIN_PASSWORD).send_keys('password')
        time.sleep(1)
        self.element_is_visible(self.locators.BUTTON_LOGIN).click()
        time.sleep(3)




