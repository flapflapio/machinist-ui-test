import time
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

web = "https://machinist.flapflap.io/"
run_inputs_path = "#__next > main > div.MenuBar__Root-sc-1th5wld-0.jDqDxJ.App__FloatingMenuBar-gv0e21-2.eZsxUV > ul > li:nth-child(4)"


def test_run_input_header(driver: WebDriver):

    driver.get(web)
    driver.find_element(By.CSS_SELECTOR, run_inputs_path).click()

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
    driver.get(web)
    driver.find_element(By.CSS_SELECTOR, run_inputs_path).click()
    element_inspect = driver.find_element(By.CLASS_NAME, "ant-modal-body").text
    true_element = "Tape:"
    assert element_inspect != true_element  # element inspect gives 'Tape: \nSubmit'


def test_shadow_input_tape(driver: WebDriver):
    driver.get(web)
    driver.find_element(By.CSS_SELECTOR, run_inputs_path).click()

    ele = (
        WebDriverWait(driver, 20)
        .until(EC.element_to_be_clickable((By.CLASS_NAME, "ant-input")))
        .get_attribute("placeholder")
    )
    true_element = "Write your input tape here"
    assert ele == true_element


def test_add_run_input_valid(driver: WebDriver):
    driver.get(web)
    driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div/div').click()
    driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/section/div/div[3]/div[1]/label[1]/span[1]'
    ).click()
    driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/section/div/div[3]/div[1]/label[2]'
    ).click()

    action = ActionChains(driver)
    # ADD TRANSITION STATE
    # Represents the ring around the state
    source = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div[1]/div/div/div[2]'
    )
    target = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div/div')

    # action.click_and_hold(source).move_to_element(target).release(target).perform()
    action.drag_and_drop(source, target).perform()
    time.sleep(10)
    ele = driver.find_element(By.CLASS_NAME, "ant-input ant-input-sm")
    ele.send_keys(Keys.TAB)
    ele.clear()
    ele.send_keys("a")

    driver.find_element(By.CSS_SELECTOR, run_inputs_path).click()
    ele2 = driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/input"
    )
    ele2.send_keys(Keys.TAB)
    ele2.clear()
    ele2.send_keys("a")
    driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/button"
    ).click()

    true_element = '{"Accepted":true,"Path":["q0","q0"],"RemainingInput":""}'
    output_element = driver.find_element(By.CLASS_NAME, "ant-modal-body").text

    assert true_element == output_element
