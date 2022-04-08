from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from config import MAIN_PAGE_FILE, driverWait
from .test_signup import login


def test_file_storage(driver: WebElement):
    login(driver, MAIN_PAGE_FILE)
    driverWait(driver, "/html/body/div[1]/div/div/div/button")
    driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/button"
    ).click()


def test_delete_file(driver: WebElement):
    login(driver, MAIN_PAGE_FILE)
    driverWait(driver, "/html/body/div[1]/div/div/div/button")
    driverWait(
        driver,
        "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[4]/span",
    )
