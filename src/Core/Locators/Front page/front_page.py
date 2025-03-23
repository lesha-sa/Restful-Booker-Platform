from selenium.webdriver.common.by import By


class FrontPage:

    BUTTON_BOOK_THIS_ROOM = (By.CSS_SELECTOR, 'button[class = "btn btn-outline-primary float-right openBooking"]')
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, 'input[class="form-control room-firstname"]')
    INPUT_LAST_NAME = (By.CSS_SELECTOR, 'input[class="form-control room-lastname"]')
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input[class="form-control room-email"]')
    INPUT_PHONE = (By.CSS_SELECTOR, 'input[class="form-control room-phone"]')
    BUTTON_BOOK = (By.CSS_SELECTOR, 'button[class="btn btn-outline-primary float-right book-room"]')
    BUTTON_CANCEL = (By.CSS_SELECTOR, 'button[class="btn btn-outline-danger float-right book-room"]')
