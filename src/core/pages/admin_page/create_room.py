import random
import time


from src.core.locators.admin_page.locators import AdminPageLocators
from src.core.pages.base_page import BasePage


class AdminPageCreateRoom(BasePage):
    locators = AdminPageLocators

    def admin_page_create_room(self):
           self.element_is_visible(self.locators.INPUT_NUMBER_OF_ROOM).send_keys(random.randint(1, 999))
           self.open_type_of_room_drop_down()
           self.element_is_visible(self.locators.TYPE_OF_ROOM_TWIN).click()
           self.element_is_visible(self.locators.SELECT_ACCESSIBLE_TRUE).click()
           self.element_is_visible(self.locators.INPUT_PRICE).send_keys(random.randint(1, 999))
           self.element_is_visible(self.locators.WIFI_CHECKBOX).click()
           self.element_is_visible(self.locators.TV_CHECKBOX_TEXT).click()
           self.element_is_visible(self.locators.CREATE_ROOM).click()
           time.sleep(5)

    def open_type_of_room_drop_down(self):
        self.element_is_visible(self.locators.TYPE_OF_ROOM).click()