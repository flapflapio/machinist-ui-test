from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

web = "https://machinist.flapflap.io/"


def test_add_node(driver: WebDriver):

    driver.get(web)
    canvas_element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]')
    action = ActionChains(driver)
    action.move_to_element_with_offset(
        canvas_element, 100, 100
    ).double_click().perform()

    # check if node is added by verifying if there is text q1
    inspect_val = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div[1]/div/div/p'
    ).text

    assert inspect_val == "q0"


def test_start_node(driver: WebDriver):
    driver.get(web)

    canvas_element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]')
    action = ActionChains(driver)
    # Adding q0 theoretically even if bug is present
    action.move_to_element_with_offset(
        canvas_element, 100, 100
    ).double_click().perform()

    # Finds q0
    driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div/div').click()
    # clicks on start state from the menu
    driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/section/div/div[3]/div[1]/label[1]/span[1]'
    ).click()
    try:
        # This part checks if the arrow is present once we select the node as start
        driver.find_element(
            By.XPATH, '//*[@id="__next"]/main/div[1]/div/div/svg/g/path[1]'
        )
    except NoSuchElementException:
        return False
    return True
