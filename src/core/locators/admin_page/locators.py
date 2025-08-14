from selenium.webdriver.common.by import By
import re


class AdminPageLocators:
    """
    Class contains the locators for the elements on the Admin Page
    """


    # loging
    INPUT_LOGIN_USER_NAME = (By.CSS_SELECTOR, 'input[id="username"]')
    INPUT_LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input[id="password"]')
    BUTTON_LOGIN = (By.CSS_SELECTOR, 'button[type="submit"]')

    # create room
    INPUT_NUMBER_OF_ROOM = (By.CSS_SELECTOR, 'input[id="roomName"]')
    TYPE_OF_ROOM = (By.CSS_SELECTOR, 'select[id="type"]')
    CREATE_ROOM_BUTTON = (By.CSS_SELECTOR, 'button[id="createRoom"]')
    CHECK_CREATE_ROOM_BY_NUMBER = (By.XPATH, "//p[text()='{number}']")

    # --- Room type options ---
    TYPE_OF_ROOM_SINGLE = (By.CSS_SELECTOR, 'option[value="Single"]')
    TYPE_OF_ROOM_TWIN = (By.CSS_SELECTOR, 'option[value="Twin"]')
    TYPE_OF_ROOM_DOUBLE = (By.CSS_SELECTOR, 'option[value="Double"]')
    TYPE_OF_ROOM_FAMILY = (By.CSS_SELECTOR, 'option[value="Family"]')
    TYPE_OF_ROOM_SUITE = (By.CSS_SELECTOR, 'option[value="Suite"]')

    TYPE_ROOM_LOCATORS = {
        "Single": (By.CSS_SELECTOR, 'option[value="Single"]'),
        "Twin": (By.CSS_SELECTOR, 'option[value="Twin"]'),
        "Double": (By.CSS_SELECTOR, 'option[value="Double"]'),
        "Family": (By.CSS_SELECTOR, 'option[value="Family"]'),
        "Suite": (By.CSS_SELECTOR, 'option[value="Suite"]'),
    }

    # --- Accessible options ---
    SELECT_ACCESSIBLE = (By.CSS_SELECTOR, 'select[id="accessible"]')
    SELECT_ACCESSIBLE_TRUE = (By.CSS_SELECTOR, 'option[value="true"]')
    SELECT_ACCESSIBLE_FALSE = (By.CSS_SELECTOR, 'option[value="false"]')

    # --- Checkbox IDs ---
    INPUT_PRICE = (By.CSS_SELECTOR, 'input[id="roomPrice"]')
    WIFI_CHECKBOX_TEXT = (By.CSS_SELECTOR, 'label[for="wifiCheckbox"]')
    WIFI_CHECKBOX = (By.CSS_SELECTOR, 'input[id="wifiCheckbox"]')
    REFRESHMENTS_CHECKBOX_TEXT = (By.CSS_SELECTOR, 'label[for="refreshCheckbox"]')
    REFRESHMENTS_CHECKBOX = (By.CSS_SELECTOR, 'input[id="refreshCheckbox"]')
    TV_CHECKBOX_TEXT = (By.CSS_SELECTOR, 'label[for="tvCheckbox"]')
    TV_CHECKBOX = (By.CSS_SELECTOR, 'input[id="tvCheckbox"]')
    SAFE_CHECKBOX_TEXT = (By.CSS_SELECTOR, 'label[for="safeCheckbox"]')
    SAFE_CHECKBOX = (By.CSS_SELECTOR, 'input[id="safeCheckbox"]')
    RADIO_CHECKBOX_TEXT = (By.CSS_SELECTOR, 'label[for="radioCheckbox"]')
    RADIO_CHECKBOX = (By.CSS_SELECTOR, 'input[id="radioCheckbox"]')
    VIEWS_CHECKBOX_TEXT = (By.CSS_SELECTOR, 'label[for="viewsCheckbox"]')
    VIEWS_CHECKBOX = (By.CSS_SELECTOR, 'input[id="viewsCheckbox"]')
    CHECKBOX_IDS = {
        "wifi": "wifiCheckbox",
        "refreshments": "refreshCheckbox",
        "tv": "tvCheckbox",
        "safe": "safeCheckbox",
        "radio": "radioCheckbox",
        "views": "viewsCheckbox",
    }

    # DELETE_ROOM = (By.CSS_SELECTOR, 'span[id="3"]')

    @staticmethod
    def normalize_key(key: str) -> str:
        """Leaves only letters and digits in the string, brings it to lower case"""
        clear_key = re.sub(r'[^a-zA-Z0-9]', '', key)
        return clear_key

    @staticmethod
    def type_of_room(room_type):
        """Dynamic locator for room type selection"""
        return (By.CSS_SELECTOR, f'option[value="{room_type}"]')

    @staticmethod
    def type_accessible(accessible):
        """Dynamic locator for accessible option selection."""
        return (By.CSS_SELECTOR, f'option[value="{accessible}"]')


    @staticmethod
    def set_room_details(room_details):
        """Returns locator for room detail checkbox label."""
        clear_room_details_key = AdminPageLocators.normalize_key(room_details)
        room_details_id = AdminPageLocators.CHECKBOX_IDS[clear_room_details_key.lower()]
        return (By.CSS_SELECTOR, f'label[for="{room_details_id}"]')
