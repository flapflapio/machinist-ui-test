from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementNotSelectableException,
    ElementNotVisibleException,
)

MAIN_PAGE_FILE = "http://localhost:3000/filestorage"
MAIN_PAGE = "http://localhost:3000/"
MAIN_PAGE_ACCOUNTS = "http://localhost:3000/accounts"
EMAIL = "flapmachinist@gmail.com"
PASSWORD = "hello123"
USERNAME = "machinist"


def driverWait(driver: WebElement, str):
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException],
    )
    element = wait.until(EC.element_to_be_clickable((By.XPATH, str)))
    element.click()
