import time

from src.core.pages.base_page import BasePage
from src.core.locators.front_page.locators import FrontPageLocators

class BookRoom(BasePage):

    locators = FrontPageLocators()

    def book_room(self):
        self.element_is_visible(self.locators.BUTTON_BOOK_NOW_IN_WELCOME_MESSAGE).click()
        #time.sleep(1)
        print('wlc button')
        self.element_is_visible(self.locators.BUTTON_CHECK_AVAILABILITY).click()
        print('chc button')
        time.sleep(1)
        self.element_is_visible(self.locators.BUTTON_BOOK_NOW_IN_OUR_ROOMS).click()
        time.sleep(1)
        self.element_is_visible(self.locators.CHOOSE_DATE_NEXT).click()
        time.sleep(1)
        self.element_is_visible(self.locators.TOTAL)
        time.sleep(1)
        self.element_is_present(self.locators.BUTTON_RESERVE_NOW_IN_ROOM_DESCRIPTION).click()
        time.sleep(1)
        self.element_is_visible(self.locators.INPUT_FIRST_NAME).send_keys('First')
        self.element_is_visible(self.locators.INPUT_LAST_NAME).send_keys('Last')
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys('email@email.com')
        self.element_is_visible(self.locators.INPUT_PHONE).send_keys('1234567890111')
        time.sleep(1)
        self.element_is_visible(self.locators.BUTTON_RESERVE_NOW_IN_PERSONAL_INFORMATION).click()
        time.sleep(1)
        booking_confirmed = self.go_up(self.locators.BOOKING_CONFIRMED).text
        time.sleep(1)
        self.element_is_visible(self.locators.BUTTON_RETURN_HOME).click()
        return booking_confirmed