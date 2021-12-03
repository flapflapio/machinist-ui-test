from typing import Generator

import pytest
from options import OPTIONS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session", autouse=True)
def driver() -> Generator[WebDriver, None, None]:
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=OPTIONS,
    )
    yield driver
    driver.quit()
