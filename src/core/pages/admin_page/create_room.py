import random

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
                logger.debug(f"Generated room number: {room_number}")

            logger.debug(f"Start creating room {room_number}")
            self.input_room_data(room_number)
            logger.success(f"Room {room_number} successfully created")
            return room_number

        except Exception as e:
            logger.error(f"Room creation error {room_number or ''}: {e}")
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
            logger.debug(f"Checking if room {room_number} exists on the page")
            return self.element_is_visible(locator, timeout=10)
        except Exception as e:
            logger.error(f"Room {room_number} not found: {e}")
            raise

    def generate_room_number(self):
        """Generating a random room number"""
        room_number = random.randint(1, 999)
        return room_number

    def input_room_number(self, number_of_room):
        """Entering a room number"""
        self.element_is_visible(self.locators.INPUT_NUMBER_OF_ROOM).send_keys(number_of_room)
        logger.debug(f"Entered room number: {number_of_room}")

    def open_type_of_room_drop_down_and_choose(self):
        """Choosing the type of room"""
        self.element_is_visible(self.locators.TYPE_OF_ROOM).click()
        self.element_is_visible(self.locators.TYPE_OF_ROOM_TWIN).click()
        logger.debug("Selected room type: Twin")

    def set_accessibility(self):
        """Setting accessibility"""
        self.element_is_visible(self.locators.SELECT_ACCESSIBLE_TRUE).click()
        logger.debug("Set accessibility to True")

    def set_random_price_room(self):
        """Setting a random price"""
        price = random.randint(1, 999)
        self.element_is_visible(self.locators.INPUT_PRICE).clear()
        self.element_is_visible(self.locators.INPUT_PRICE).send_keys(price)
        logger.debug(f"Set room price: {price}")
        return price

    def select_additional_services(self):
        """Choosing additional services"""
        self.element_is_visible(self.locators.WIFI_CHECKBOX).click()
        logger.debug(f"Selected service: WIFI")
        self.element_is_visible(self.locators.TV_CHECKBOX_TEXT).click()
        logger.debug(f"Selected service: TV")

    def submit_creation_room(self):
        """Submitting the room creation form"""
        self.element_is_visible(self.locators.CREATE_ROOM_BUTTON).click()
        logger.debug("Submitted the room creation form")
