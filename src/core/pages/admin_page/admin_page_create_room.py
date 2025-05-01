import time
import random

from src.core.locators.admin_page.admin_page_locators import AdminPageLocators
from src.core.pages.base_page import BasePage


class AdminPageCreateRoom(BasePage):
    locators = AdminPageLocators

    def admin_page_loging(self):
        self.element_is_visible(self.locators.INPUT_LOGIN_USER_NAME).send_keys('admin')
        time.sleep(1)
        self.element_is_visible(self.locators.INPUT_LOGIN_PASSWORD).send_keys('password')
        time.sleep(1)
        self.element_is_visible(self.locators.BUTTON_LOGIN).click()
        time.sleep(3)

    def admin_page_create_room(self):
        self.element_is_visible(self.locators.INPUT_NUMBER_OF_ROOM).send_keys(random.randint(1, 999))
        self.element_is_visible(self.locators.TYPE_OF_ROOM).click()
        self.element_is_visible(self.locators.TYPE_OF_ROOM_TWIN).click()
        self.element_is_visible(self.locators.SELECT_ACCESSIBLE_TRUE).click()
        self.element_is_visible(self.locators.INPUT_PRICE).send_keys(random.randint(1, 999))
        self.element_is_visible(self.locators.WIFI_CHECKBOX).click()
        self.element_is_visible(self.locators.TV_CHECKBOX_TEXT).click()
        self.element_is_visible(self.locators.CREATE_ROOM).click()
        time.sleep(5)


