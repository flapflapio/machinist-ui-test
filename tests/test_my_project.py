from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import logging

LOGGER = logging.getLogger(__name__)


def test_python_dot_org(driver: WebDriver):
    """This is a demo test that shows basic usage of selenium.

    Args:
        driver (WebDriver): The WebDriver test fixture. Injected by pytest.
    """

    driver.get("https://www.python.org")

    # Enter a search
    ele = driver.find_element(By.TAG_NAME, "#id-search-field").
    ele.send_keys(Keys.TAB)
    ele.clear()
    ele.send_keys("python3")

    # Submit the search
    driver.find_element(By.CSS_SELECTOR, "#submit").click()

    # Grab the first search result
    search_results = driver.find_element(By.CSS_SELECTOR, ".list-recent-events")
    first_result = search_results.find_element(By.CSS_SELECTOR, "a")

    # Assert that the first search result is some text...
    assert first_result.text == 'PEP 394 -- The "python" Command on Unix-Like Systems'


def test_expanding_menu_bar(driver: WebDriver):

    driver.get("https://machinist.flapflap.io/")

    menu_bar = driver.find_element(By.XPATH, r'.//*[contains(@class,"MenuBar__Root")]')

    size = menu_bar.size

    driver.find_element(
        By.XPATH, r'.//*[contains(@class,"MenuBar__ToggleButton")]'
    ).click()

    assert size["width"] < menu_bar.size["width"]

    driver.find_element(
        By.XPATH, r'.//*[contains(@class,"MenuBar__ToggleButton")]'
    ).click()

    assert menu_bar.size["width"] == size["width"]


def test_tool_tip(driver: WebDriver):

    driver.get("https://machinist.flapflap.io/")
    list_items: List[WebElement] = driver.find_element(
        By.CSS_SELECTOR,
        ".ant-menu.ant-menu-light.ant-menu-inline-collapsed.ant-menu-root",
    ).find_elements(By.TAG_NAME, "li")

    actions = ActionChains(driver)

    for i in range(3):
        before_hover: str = list_items[i].get_attribute("class")
        updated_elements: List[WebElement] = driver.find_elements(
            By.CSS_SELECTOR, "." + before_hover
        )
        actions.move_to_element(updated_elements[i]).perform()
        updated_class: str = updated_elements[i].get_attribute("class")
        assert (before_hover != updated_class and "ant-tooltip-open" in updated_class)


def test_submenus(driver: WebDriver):
    driver.get("https://machinist.flapflap.io/")

    actions = ActionChains(driver)

    sub_menu: WebElement = driver.find_element(By.CSS_SELECTOR, ".ant-menu-submenu.ant-menu-submenu-vertical")

    previous_class: str = sub_menu.get_attribute("class")

    hidden_option_menu: WebElement = driver.find_elements(By.CSS_SELECTOR, ".ant-menu-submenu.ant-menu-submenu-popup")

    if(len(hidden_option_menu) > 0):
        assert False

    actions.move_to_element(sub_menu).perform()

    new_class: str = driver.find_element(By.CSS_SELECTOR, ".ant-menu-submenu.ant-menu-submenu-vertical").get_attribute("class")

    assert previous_class != new_class and previous_class in new_class and 'ant-menu-submenu-open' in new_class

    assert "ant-menu-hidden" not in driver.find_element(By.CSS_SELECTOR, ".ant-menu-submenu.ant-menu-submenu-popup").get_attribute("class")

    actions.move_to_element(driver.find_element(By.XPATH,r'.//*[contains(@class,"MenuBar__ToggleButton")]')).perform()

    assert "ant-menu-hidden" in driver.find_element(By.CSS_SELECTOR, ".ant-menu-submenu.ant-menu-submenu-popup").get_attribute("class")


def test_open_close_debugger(driver: WebDriver):
    driver.get("https://machinist.flapflap.io/")

    driver.find_element(By.CSS_SELECTOR, ".ant-menu-item").click()

    items: int = len(driver.find_elements(
        By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]'
    ))

    if(items != 1):
        assert False

    driver.find_element(
        By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__CloseDebuggerButton")]'
    ).click()

    items: int = len(driver.find_elements(
        By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]'
    ))

    assert items == 0

def test_move_debugger(driver: WebElement):
    driver.get("https://machinist.flapflap.io/")

    driver.find_element(By.CSS_SELECTOR, ".ant-menu-item").click()

    if(len(driver.find_elements(By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]')) != 1):
        assert False

    previous_dragabble: str = driver.find_element(By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]').get_attribute("style")
    
    actions = ActionChains(driver)

    element: WebElement = driver.find_element(By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]')

    actions.drag_and_drop_by_offset(element, -419, 318).perform()
    
    after_dragabble: str = driver.find_element(By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]').get_attribute("style")

    assert previous_dragabble != after_dragabble
    