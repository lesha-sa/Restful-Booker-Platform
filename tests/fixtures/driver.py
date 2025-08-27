import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse

from config.logger.config_logger import get_logger
from src.db.connector import is_resolvable

logger = get_logger()


@pytest.fixture(scope='function')
def driver():
    """
        Returns a Selenium WebDriver instance.
        If SELENIUM_URL is set and resolvable, uses Remote WebDriver.
        Otherwise, starts a local Chrome browser.
        The browser is automatically closed after the test.
    """
    selenium_url = os.getenv('SELENIUM_URL')
    options = Options()
    options.add_argument("--start-maximized")

    # If SELENIUM_URL is set and its host is accessible over the network:
    #   - urlparse(...).hostname extracts the host name from the URL (e.g., ‘selenium’)
    #   - is_resolvable(host) checks that this host can be found on the network (DNS/resolution)
    # That is, you can connect to remote Selenium.
    if selenium_url and is_resolvable(urlparse(selenium_url).hostname):
        logger.info(f"Starting Remote WebDriver at {selenium_url}")
        driver_instance = webdriver.Remote(command_executor=selenium_url, options=options)
    else:
        # Otherwise, launch the local Chrome browser.
        logger.info("Starting local Chrome WebDriver")
        driver_instance = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    yield driver_instance
    driver_instance.quit()
    logger.info("Browser closed")
