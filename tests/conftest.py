import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    selenium_url = os.getenv('SELENIUM_URL')
    options = Options()
    options.add_argument("--start-maximized")
    if selenium_url:
        driver = webdriver.Remote(command_executor=selenium_url, options=options)
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    yield driver
    driver.quit()
