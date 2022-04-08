from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from config import EMAIL, PASS, MAIN_PAGE


def login(driver: WebElement, str):
    driver.get(str)
    email_box = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div/div[2]/div/div/form/div/fieldset/div[1]/div/div/input",
    )
    email_box.send_keys(Keys.TAB)
    email_box.clear()
    email_box.send_keys(EMAIL)

    password_box = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div/div[2]/div/div/form/div/fieldset/div[2]/div/div[1]/input",
    )
    password_box.send_keys(Keys.TAB)
    password_box.clear()
    password_box.send_keys(PASS)

    driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div/div[2]/div/div/form/div/button",
    ).click()


def test_signup(driver: WebElement):
    login(driver, MAIN_PAGE)
