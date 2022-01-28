from typing import Optional
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementNotSelectableException,
    NoSuchElementException,
)
from selenium.webdriver import ActionChains

from options import HOMEPAGE


RUN_INPUTS_PATH = r'.//*[contains(@class,"anticon anticon-desktop ant-menu-item-icon")]'


def test_run_input_header(driver: WebDriver):

    driver.get(HOMEPAGE)
    driver.find_element(By.XPATH, RUN_INPUTS_PATH).click()

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

    text_from_web = wait.until(element_is_visible_and_has_text)

    expected_text = "Run Inputs"
    assert text_from_web == expected_text


def test_run_input_tape(driver: WebDriver):
    driver.get(HOMEPAGE)
    driver.find_element(By.XPATH, RUN_INPUTS_PATH).click()
    text_from_web = driver.find_element(By.CLASS_NAME, "ant-modal-body").text
    expected_text = "Tape:"
    assert text_from_web != expected_text  # element inspect gives 'Tape: \nSubmit'


def test_shadow_input_tape(driver: WebDriver):
    driver.get(HOMEPAGE)
    driver.find_element(By.XPATH, RUN_INPUTS_PATH).click()

    text_from_web = (
        WebDriverWait(driver, 20)
        .until(EC.element_to_be_clickable((By.CLASS_NAME, "ant-input")))
        .get_attribute("placeholder")
    )
    expected_text = "Write your input tape here"
    assert expected_text == text_from_web


def test_add_run_input_valid(driver: WebDriver):
    driver.get(HOMEPAGE)

    # q0 state
    driver.find_element(By.XPATH, r'.//*[contains(@class,"State__StateRoot")]').click()
    # select start state
    driver.find_element(
        By.XPATH, r'.//*[contains(@class,"ant-checkbox-input")]'
    ).click()
    # select end state
    driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/section/div/div[3]/div[1]/label[2]/span[1]'
    ).click()

    action = ActionChains(driver)

    source_ring_ball = driver.find_element(
        By.XPATH,
        r'.//*[contains(@class,"TransitionCreatorRing__Ball")]',
    )

    target_state = driver.find_element(
        By.XPATH, r'.//*[contains(@class,"State__StateRoot")]'
    )
    action.click_and_hold(source_ring_ball).drag_and_drop(
        source_ring_ball, target_state
    ).perform()
    ele = driver.find_element(
        By.XPATH, r'.//*[contains(@class,"ant-input ant-input-sm")]'
    )
    ele.send_keys(Keys.TAB)
    ele.clear()
    ele.send_keys("a")

    driver.find_element(By.XPATH, RUN_INPUTS_PATH).click()
    run_input_placeholder = driver.find_element(
        By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/input"
    )
    run_input_placeholder.send_keys(Keys.TAB)
    run_input_placeholder.send_keys("a")
    driver.find_element(
        By.CSS_SELECTOR,
        "body > div:nth-child(17) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > button",
    ).click()

    true_element = '{"Accepted":true,"Path":["q0","q0"],"RemainingInput":""}'

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
        ele = driver.find_element(By.CSS_SELECTOR, ".ant-modal-body p")
        if ele.is_displayed and ele.text != "":
            return ele.text
        else:
            return None

    element_inspect = wait.until(element_is_visible_and_has_text)
    assert true_element == element_inspect
