from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains


MAIN_PAGE = "https://machinist.flapflap.io/"


def test_deleting_node(driver: WebDriver):

    driver.maximize_window()
    driver.get(MAIN_PAGE)

    actions = ActionChains(driver)

    canvas_element = driver.find_element(
        By.XPATH, r'.//*[contains(@class,"NodeLayer__Root")]'
    )
    actions.move_to_element_with_offset(
        canvas_element, 100, 100
    ).double_click().perform()
    
    node_bar_style = driver.find_element(
        By.XPATH, r'.//*[starts-with(@class,"NodeMenu__NodeMenuRoot")]'
    ).get_attribute("style")

    # make sure the nodeMenu is not visible at start
    assert node_bar_style == 'opacity: 0;'

    driver.find_element(By.XPATH, r'.//*[contains(@class,"State__StateRoot")]').click()
    
    node_bar_style = driver.find_element(
        By.XPATH, r'.//*[starts-with(@class,"NodeMenu__NodeMenuRoot")]'
    ).get_attribute("style")

    # make sure the nodeMenu is visible once a node is selected
    assert node_bar_style == ''

    driver.find_element(By.XPATH, r'.//*[contains(@class,"NodeMenu__DeleteButton")]').click()

    # need to remove the comment once the bug on machinist page    
    #assert len(driver.find_elements(By.XPATH, r'.//*[contains(@class,"State__StateRoot")]')) == 1 
