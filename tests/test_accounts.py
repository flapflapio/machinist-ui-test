from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from config import EMAIL, PASSWORD, USERNAME, MAIN_PAGE_ACCOUNTS, driverWait
from .test_signup import login


def test_account_modify(driver: WebElement):
    login(driver, MAIN_PAGE_ACCOUNTS)
    driverWait(driver, "/html/body/div[1]/div/div/div/div/div[1]/button")

    username_box = driver.find_element(
        By.XPATH,
        "/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/form/div[1]/div[2]/div/div/input",
    )
    username_box.send_keys(Keys.TAB)
    username_box.clear()
    username_box.send_keys(USERNAME)

    email_box2 = driver.find_element(
        By.XPATH,
        "/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/form/div[2]/div[2]/div/div/input",
    )
    email_box2.send_keys(Keys.TAB)
    email_box2.clear()
    email_box2.send_keys(EMAIL)

    password_box2 = driver.find_element(
        By.XPATH,
        "/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/form/div[3]/div[2]/div/div/span/input",
    )
    password_box2.send_keys(Keys.TAB)
    password_box2.clear()
    password_box2.send_keys(PASSWORD)

    driver.find_element(
        By.XPATH,
        "/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/form/div[4]/div/div/div/button",
    ).click()
    driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/button"
    ).click()
