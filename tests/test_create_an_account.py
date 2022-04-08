from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from config import EMAIL, PASSWORD, MAIN_PAGE


def testCreateAccount(driver: WebElement):
    driver.get(MAIN_PAGE)
    driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/button[2]"
    ).click()

    email_box = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div/div[3]/div/div/form/fieldset/div/div[1]/div/div/input",
    )
    email_box.send_keys(Keys.TAB)
    email_box.clear()
    email_box.send_keys(EMAIL)

    password_box = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div/div[3]/div/div/form/fieldset/div/div[2]/div/div[1]/input",
    )
    password_box.send_keys(Keys.TAB)
    password_box.clear()
    password_box.send_keys(PASSWORD)

    password_confirmation = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div/div[3]/div/div/form/fieldset/div/div[3]/div/div[1]/input",
    )
    password_confirmation.send_keys(Keys.TAB)
    password_confirmation.clear()
    password_confirmation.send_keys(PASSWORD)

    driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div/div[3]/div/div/form/fieldset/button",
    ).click()
