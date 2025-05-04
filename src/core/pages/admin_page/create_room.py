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
        self.element_is_visible(self.locators.INPUT_NUMBER_OF_ROOM).send_keys(random.randint(1, 999))
        logger.debug('input number of room')
        self.open_type_of_room_drop_down()
        logger.debug('open type of room drop down')
        self.element_is_visible(self.locators.TYPE_OF_ROOM_TWIN).click()
        logger.debug('choice type of room twin')
        self.element_is_visible(self.locators.SELECT_ACCESSIBLE_TRUE).click()
        logger.debug('select accessible true')
        self.element_is_visible(self.locators.INPUT_PRICE).send_keys(random.randint(1, 999))
        logger.debug('input price')
        self.element_is_visible(self.locators.WIFI_CHECKBOX).click()
        logger.debug('WIFI checkbox')
        self.element_is_visible(self.locators.TV_CHECKBOX_TEXT).click()
        logger.debug('TV check box')
        self.element_is_visible(self.locators.CREATE_ROOM).click()
        logger.debug('click button create room')
        time.sleep(2)

    def open_type_of_room_drop_down(self):
        self.element_is_visible(self.locators.TYPE_OF_ROOM).click()
