from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

MAIN_PAGE = "http://localhost:3000/accounts"


def test_account_modify(driver: WebElement):
    driver.get(MAIN_PAGE)
    username = "machinist"
    email = "flapmachinist@gmail.com"
    password = "hello123"
    email_box = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div/div[2]/div/div/form/div/fieldset/div[1]/div/div/input",
    )
    email_box.send_keys(Keys.TAB)
    email_box.clear()
    email_box.send_keys(email)

    password_box = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div/div[2]/div/div/form/div/fieldset/div[2]/div/div[1]/input",
    )
    password_box.send_keys(Keys.TAB)
    password_box.clear()
    password_box.send_keys(password)
    driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div/div[2]/div/div/form/div/button",
    ).click()
    driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div/div[1]/button",
    ).click()

    username_box = driver.find_element(
        By.XPATH,
        "/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/form/div[1]/div[2]/div/div/input",
    )
    username_box.send_keys(Keys.TAB)
    username_box.clear()
    username_box.send_keys(username)

    email_box2 = driver.find_element(
        By.XPATH,
        "/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/form/div[2]/div[2]/div/div/input",
    )
    email_box2.send_keys(Keys.TAB)
    email_box2.clear()
    email_box2.send_keys(email)

    password_box2 = driver.find_element(
        By.XPATH,
        "/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/form/div[3]/div[2]/div/div/span/input",
    )
    password_box2.send_keys(Keys.TAB)
    password_box2.clear()
    password_box2.send_keys(password)

    driver.find_element(
        By.XPATH,
        "/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/form/div[4]/div/div/div/button",
    ).click()
    driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/button"
    ).click()
