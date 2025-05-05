import random
import time
from config.logger.config_logger import get_logger

from src.core.locators.admin_page.locators import AdminPageLocators
from src.core.pages.admin_page.logging_admin_panel import logger
from src.core.pages.base_page import BasePage

logger = get_logger()

class AdminPageCreateRoom(BasePage):
    locators = AdminPageLocators

    def admin_page_create_room(self):
        room_number = self.input_number_of_room()
        self.open_type_of_room_drop_down_and_choose()
        self.accessible_and_price()
        self.select_additional_services()
        time.sleep(2)
        #nr = room_number
        #text = find_element('xpath',  f'//p[text()="{nr}"]')
        return room_number #, text

    def input_number_of_room(self):
        room_number = random.randint(1, 999)
        self.element_is_visible(self.locators.INPUT_NUMBER_OF_ROOM).send_keys(room_number)
        logger.debug('input number of room')
        return room_number

    def open_type_of_room_drop_down_and_choose(self):
        self.element_is_visible(self.locators.TYPE_OF_ROOM).click()
        logger.debug('open type of room drop down')
        self.element_is_visible(self.locators.TYPE_OF_ROOM_TWIN).click()
        logger.debug('choice type of room twin')

    def accessible_and_price(self):
        self.element_is_visible(self.locators.SELECT_ACCESSIBLE_TRUE).click()
        logger.debug('select accessible true')
        self.element_is_visible(self.locators.INPUT_PRICE).send_keys(random.randint(1, 999))
        logger.debug('input price')

    def select_additional_services(self):
        self.element_is_visible(self.locators.WIFI_CHECKBOX).click()
        logger.debug('WIFI checkbox')
        self.element_is_visible(self.locators.TV_CHECKBOX_TEXT).click()
        logger.debug('TV check box')
        self.element_is_visible(self.locators.CREATE_ROOM).click()
        logger.debug('click button create room')
