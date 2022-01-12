from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementNotSelectableException,
    NoSuchElementException,
)
import time

web = "https://machinist.flapflap.io/"


def test_run_input_header(driver: WebDriver):

    driver.get(web)
    driver.find_element_by_xpath('//*[@id="__next"]/main/div[2]/ul/li[2]').click()

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            ElementNotVisibleException,
            ElementNotSelectableException,
            NoSuchElementException,
        ],
    )

    def element_is_visible_and_has_text(driver: WebDriver) -> Optional[str]:
        ele = driver.find_element(By.XPATH, '//*[@id="rcDialogTitle0"]')
        if ele.is_displayed and ele.text != "":
            return ele.text
        else:
            return None

    element_inspect = wait.until(element_is_visible_and_has_text)

    true_element = "Run Inputs"
    assert element_inspect == true_element


def test_run_input_tape(driver: WebDriver):
    driver.get("https://machinist.flapflap.io/")
    driver.find_element_by_xpath('//*[@id="__next"]/main/div[2]/ul/li[2]').click()
    WebDriverWait(driver, 5)
    element_inspect = driver.find_element_by_class_name("ant-modal-body").text
    true_element = "Tape:"
    assert element_inspect != true_element  # element inspect gives 'Tape: \nSubmit'


def test_shadow_input_tape(driver: WebDriver):
    driver.get("https://machinist.flapflap.io/")
    driver.find_element_by_xpath('//*[@id="__next"]/main/div[2]/ul/li[2]').click()
    time.sleep(5)

    ele = (
        WebDriverWait(driver, 20)
        .until(EC.element_to_be_clickable((By.CLASS_NAME, "ant-input")))
        .get_attribute("placeholder")
    )

    # ele = driver.find_element(By.CLASS_NAME, "ant-modal-body").get_attribute("value")
    true_element = "Write your input tape here"
    assert ele == true_element
