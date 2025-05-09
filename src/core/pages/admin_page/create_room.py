import random
import time

from config.logger.config_logger import get_logger

from src.core.locators.admin_page.locators import AdminPageLocators
from src.core.pages.base_page import BasePage

logger = get_logger()


class AdminPageCreateRoom(BasePage):
    locators = AdminPageLocators

    def admin_page_create_room(self, room_number=None):
        """Creating a new room"""
        try:
            if room_number is None:
                room_number = self.generate_room_number()
                logger.debug(f"Generation of room number: {room_number}")

            logger.debug(f"The beginning of creating a room {room_number}")
            self.input_room_data(room_number)
            logger.success(f"Room {room_number} successfully established")
            return room_number

        except Exception as e:
            logger.error(f"Room creation error {room_number or ''}: {str(e)}")
            raise

    def input_room_data(self, room_number):
        """Entering room data"""
        self.input_room_number(room_number)
        self.open_type_of_room_drop_down_and_choose()
        self.set_accessibility()
        self.set_random_price_room()
        self.select_additional_services()
        self.submit_creation_room()

    def check_created_room(self, room_number):
        try:
            locator = (self.locators.CHECK_CREATE_ROOM_BY_NUMBER[0],
                       self.locators.CHECK_CREATE_ROOM_BY_NUMBER[1].format(number=room_number))
            logger.debug(f"Found number in the interface: {room_number}")
            return self.element_is_visible(locator, timeout=10)
        except Exception as e:
            logger.error(f"Room {room_number} not found: {str(e)}")
            raise

    def generate_room_number(self):
        """Generating a random room number"""
        room_number = random.randint(1, 999)
        return room_number

    def input_room_number(self, number_of_room):
        """Entering a room number"""
        self.element_is_visible(self.locators.INPUT_NUMBER_OF_ROOM).send_keys(number_of_room)
        logger.debug(f"Room number entered: {number_of_room}")

    def open_type_of_room_drop_down_and_choose(self):
        """Choosing the type of room"""
        self.element_is_visible(self.locators.TYPE_OF_ROOM).click()
        self.element_is_visible(self.locators.TYPE_OF_ROOM_TWIN).click()
        logger.debug("Room type selected: Twin")

    def set_accessibility(self):
        """Установка доступности"""
        self.element_is_visible(self.locators.SELECT_ACCESSIBLE_TRUE).click()
        logger.debug("Accessibility setting: True")

    def set_random_price_room(self):
        """Setting a random price"""
        price = random.randint(1, 999)
        self.element_is_visible(self.locators.INPUT_PRICE).clear()
        self.element_is_visible(self.locators.INPUT_PRICE).send_keys(price)
        logger.debug(f"The price is set: {price}")
        return price

    def select_additional_services(self):
        """Choice of additional services"""
        self.element_is_visible(self.locators.WIFI_CHECKBOX).click()
        logger.debug(f"Service selected: WIFI")
        self.element_is_visible(self.locators.TV_CHECKBOX_TEXT).click()
        logger.debug(f"Service selected: TV")

    def submit_creation_room(self):
        """Submitting a creation form"""
        self.element_is_visible(self.locators.CREATE_ROOM).click()
        logger.debug("Creation form has been sent")
