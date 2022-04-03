from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

MAIN_PAGE = "http://localhost:3000/filestorage"


def test_upload_file(driver: WebElement):
    driver.get(MAIN_PAGE)
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
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/button").click()
    driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/button"
    ).click()


def test_delete_file(driver: WebElement):
    driver.get(MAIN_PAGE)
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
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/button").click()
    driver.find_element(
        By.XPATH,
        "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[4]/span",
    ).click()
