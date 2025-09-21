import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.logger.config_logger import get_logger


logger = get_logger()


@pytest.fixture(scope='function')
def driver(request):
    """
    Selenium WebDriver fixture for Docker + local:
    - Browser selection via --browser (chrome/firefox)
    - Remote WebDriver via SELENIUM_CHROME_URL / SELENIUM_FIREFOX_URL
    - Allure parameter 'Browser'
    - Maximized window for Chrome, large window for Firefox
    """
    browser_name = request.config.getoption("--browser").lower()

    # Allure parameter
    allure.dynamic.parameter("Browser", browser_name)

    # --- Chrome options ---
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 2}
    )

    # --- Firefox options ---
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")

    # --- Docker Selenium URLs ---
    selenium_chrome_url = os.getenv("SELENIUM_CHROME_URL")
    selenium_firefox_url = os.getenv("SELENIUM_FIREFOX_URL")

    # --- Remote WebDriver ---
    if browser_name == "chrome" and selenium_chrome_url:
        logger.info(f"Connecting to remote Chrome at {selenium_chrome_url}")
        driver_instance = webdriver.Remote(command_executor=selenium_chrome_url, options=chrome_options)
    elif browser_name == "firefox" and selenium_firefox_url:
        logger.info(f"Connecting to remote Firefox at {selenium_firefox_url}")
        driver_instance = webdriver.Remote(command_executor=selenium_firefox_url, options=firefox_options)
    else:
        # --- Local fallback ---
        logger.info(f"Starting local {browser_name} WebDriver")
        if browser_name == "chrome":
            driver_instance = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=chrome_options
            )
        elif browser_name == "firefox":
            driver_instance = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=firefox_options
            )
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver_instance
    driver_instance.quit()
    logger.info(f"{browser_name.capitalize()} browser closed")
