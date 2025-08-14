import time

from config.logger.config_logger import get_logger
from src.schemas.room_template import RoomTemplate

from src.core.locators.admin_page.locators import AdminPageLocators
from src.core.pages.base_page import BasePage

logger = get_logger()


class AdminPageCreateRooms(BasePage):
    locators = AdminPageLocators

    def admin_page_create_room_db_data(self, room: RoomTemplate):
        """Create a new room from RoomTemplate data"""
        logger.debug(f"Creating room: {room}")
        self.input_room_number(room.room_number)
        self.select_room_type(room.room_type)
        self.select_accessibility(room.accessible)
        self.select_price(room.price)
        self.select_room_details(room.room_details)
        self.submit()
        logger.info(f"Room {room.room_number} successfully created")
        return room.room_number

    def input_room_number(self, room_number):
        self.element_is_visible(self.locators.INPUT_NUMBER_OF_ROOM).send_keys(room_number)
        logger.debug(f"Room number entered: {room_number}")

    def select_room_type(self, room_type):
        """Choose the type of room"""
        '''self.element_is_visible(self.locators.TYPE_OF_ROOM).click()
        locator = self.locators.ROOM_TYPE_LOCATORS[room_type]
        self.element_is_visible(locator).click()
        '''
        self.element_is_visible(self.locators.TYPE_OF_ROOM).click()
        self.element_is_visible(self.locators.type_of_room(room_type)).click()
        logger.debug(f"Room type selected: {room_type}")

    def select_accessibility(self, accessible):
        self.element_is_visible(self.locators.SELECT_ACCESSIBLE).click()
        self.element_is_visible(self.locators.type_accessible(accessible)).click()
        logger.debug(f"Accessibility set to: {accessible}")

    def select_price(self, price):
        self.element_is_visible(self.locators.INPUT_PRICE).send_keys(int(price))
        logger.debug(f"Room price set to: {price}")

    def select_room_details(self, room_details):
        selected_details = []
        for detail in room_details.split():
            self.element_is_visible(self.locators.set_room_details(detail)).click()
            selected_details.append(detail)
        if selected_details:
            logger.debug(f"Room details selected: {' '.join(selected_details)}")

    def submit(self):
        self.element_is_visible(self.locators.CREATE_ROOM_BUTTON).click()
        logger.debug("Room creation form submitted")


    def check_created_room(self, room_number):
        try:
            locator = (self.locators.CHECK_CREATE_ROOM_BY_NUMBER[0],
                       self.locators.CHECK_CREATE_ROOM_BY_NUMBER[1].format(number=room_number))
            logger.debug(f"Checking room on page: {room_number}")
            return self.element_is_visible(locator, timeout=10)
        except Exception as e:
            logger.error(f"Room {room_number} not found: {e}")
            raise