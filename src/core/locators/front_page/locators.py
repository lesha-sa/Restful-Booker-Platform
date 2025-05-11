from selenium.webdriver.common.by import By


class FrontPageLocators:
    """
    Class contains the locators for the elements on the Front Page
    """
    BUTTON_BOOK_NOW_IN_WELCOME_MESSAGE = (By.CSS_SELECTOR, 'a[class="btn btn-primary btn-lg"]')
    BUTTON_CHECK_AVAILABILITY = (By.CSS_SELECTOR, 'button[class="btn btn-primary w-100 py-2"]')
    BUTTON_BOOK_NOW_IN_OUR_ROOMS = (By.CSS_SELECTOR, 'a[class="btn btn-primary"]')
    BUTTON_RESERVE_NOW_IN_ROOM_DESCRIPTION = (By.CSS_SELECTOR, 'button[id="doReservation"]')
    CHOOSE_DATE_NEXT = (By.XPATH, '//button[text()="Next"]')
    TOTAL = (By.CSS_SELECTOR, 'div[class="d-flex justify-content-between fw-bold"]')
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, 'input[class="form-control room-firstname"]')
    INPUT_LAST_NAME = (By.CSS_SELECTOR, 'input[class="form-control room-lastname"]')
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input[class="form-control room-email"]')
    INPUT_PHONE = (By.CSS_SELECTOR, 'input[class="form-control room-phone"]')
    BUTTON_RESERVE_NOW_IN_PERSONAL_INFORMATION = (By.CSS_SELECTOR, 'button[class="btn btn-primary w-100 mb-3"]')
    BUTTON_CANCEL_IN_PERSONAL_INFORMATION = (By.CSS_SELECTOR, 'button[class="btn btn-secondary w-100 mb-3"]')
    BUTTON_RETURN_HOME = (By.CSS_SELECTOR, 'a[class="btn btn-primary w-100 mb-3 mt-3"]')
    BOOKING_CONFIRMED = (By.CSS_SELECTOR, 'h2[class="card-title fs-4 fw-bold mb-3"]')