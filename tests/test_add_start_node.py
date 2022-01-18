from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

web = "https://machinist.flapflap.io/"


def test_add_node(driver: WebDriver):

    driver.get(web)
    source = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]')
    action = ActionChains(driver)
    action.double_click(source).perform()

    # check if node is added by verifying if there is text q1
    inspect_val = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div[1]/div/div[2]/p'
    ).text
    true_val = "q1"

    assert inspect_val == true_val


def test_start_node(driver: WebDriver):
    driver.get(web)
    driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div/div').click()
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
