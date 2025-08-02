import os
import pytest
import socket
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from src.db.connector import get_db_connection

load_dotenv()

def is_resolvable(host: str) -> bool:
    try:
        socket.gethostbyname(host)
        return True
    except:
        return False

@pytest.fixture(scope='function')
def driver():
    selenium_url = os.getenv('SELENIUM_URL')
    options = Options()
    options.add_argument("--start-maximized")

    host = selenium_url.split("//")[-1].split(":")[0] if selenium_url else None

    if selenium_url and host and is_resolvable(host):
        driver = webdriver.Remote(command_executor=selenium_url, options=options)
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def db_connection():
    conn = get_db_connection()
    yield conn
    conn.close()
