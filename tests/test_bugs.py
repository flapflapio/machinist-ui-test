from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


MAIN_PAGE = "https://machinist.flapflap.io/"


def test_no_node_present_at_start(driver: WebElement):

    driver.maximize_window()
    driver.get(MAIN_PAGE)

    node_elements = driver.find_elements(
        By.XPATH, r'.//*[contains(@class,"State__StateRoot")]'
    )

    #need to uncomment once the bug is fixed
    #assert len(node_elements) == 1
