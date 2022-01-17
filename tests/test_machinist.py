from typing import List, Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import logging
import time

LOGGER = logging.getLogger(__name__)
MAIN_PAGE = "https://machinist.flapflap.io/"


def test_expanding_menu_bar(driver: WebDriver):
    driver.maximize_window()
    driver.get(MAIN_PAGE)

    menu_bar = driver.find_element(By.XPATH, r'.//*[contains(@class,"MenuBar__Root")]')

    size = menu_bar.size

    driver.find_element(
        By.XPATH, r'.//*[contains(@class,"MenuBar__ToggleButton")]'
    ).click()

    menu_bar = driver.find_element(By.XPATH, r'.//*[contains(@class,"MenuBar__Root")]')
    assert size["width"] < menu_bar.size["width"]


def test_menubar_same_size(driver: WebDriver):
    class wait_for_small_size:
        def __init__(self, locator: Tuple[By, str], width: int):
            self.locator = locator
            self.width = width

        def __call__(self, driver: WebDriver) -> bool:
            element = driver.find_element(*self.locator)
            ele_width = element.size["width"]
            return ele_width == self.width

    driver.maximize_window()
    driver.get(MAIN_PAGE)

    menu_bar = driver.find_element(By.XPATH, r'.//*[contains(@class,"MenuBar__Root")]')
    size = menu_bar.size["width"]

    driver.find_element(
        By.XPATH, r'.//*[contains(@class,"MenuBar__ToggleButton")]'
    ).click()

    driver.find_element(
        By.XPATH, r'.//*[contains(@class,"MenuBar__ToggleButton")]'
    ).click()

    WebDriverWait(driver, 10).until(
        wait_for_small_size((By.XPATH, r'.//*[contains(@class,"MenuBar__Root")]'), size)
    )

    menu_bar = driver.find_element(By.XPATH, r'.//*[contains(@class,"MenuBar__Root")]')
    new_size = menu_bar.size["width"]

    assert new_size == size


def test_tool_tip(driver: WebDriver):
    driver.maximize_window()
    driver.get(MAIN_PAGE)

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
        assert before_hover != updated_class and "ant-tooltip-open" in updated_class


def test_submenus(driver: WebDriver):
    driver.maximize_window()
    driver.get(MAIN_PAGE)

    actions = ActionChains(driver)

    sub_menu: WebElement = driver.find_element(
        By.CSS_SELECTOR, ".ant-menu-submenu.ant-menu-submenu-vertical"
    )
    previous_class: str = sub_menu.get_attribute("class")
    hidden_option_menu: WebElement = driver.find_elements(
        By.CSS_SELECTOR, ".ant-menu-submenu.ant-menu-submenu-popup"
    )

    if len(hidden_option_menu) > 0:
        assert False

    actions.move_to_element(sub_menu).perform()
    new_class: str = driver.find_element(
        By.CSS_SELECTOR, ".ant-menu-submenu.ant-menu-submenu-vertical"
    ).get_attribute("class")

    assert (
        previous_class != new_class
        and previous_class in new_class
        and "ant-menu-submenu-open" in new_class
    )
    assert "ant-menu-hidden" not in driver.find_element(
        By.CSS_SELECTOR, ".ant-menu-submenu.ant-menu-submenu-popup"
    ).get_attribute("class")


def test_open_close_debugger(driver: WebDriver):
    driver.maximize_window()
    driver.get(MAIN_PAGE)
    driver.find_element(By.CSS_SELECTOR, ".ant-menu-item").click()

    items: int = len(
        driver.find_elements(
            By.XPATH,
            r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]',
        )
    )

    if items != 1:
        assert False

    driver.find_element(
        By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__CloseDebuggerButton")]'
    ).click()

    items: int = len(
        driver.find_elements(
            By.XPATH,
            r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]',
        )
    )

    assert items == 0


def test_move_debugger(driver: WebElement):
    driver.maximize_window()
    driver.get(MAIN_PAGE)
    driver.find_element(By.CSS_SELECTOR, ".ant-menu-item").click()

    if (
        len(
            driver.find_elements(
                By.XPATH,
                r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]',
            )
        )
        != 1
    ):
        assert False

    previous_dragabble: str = driver.find_element(
        By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]'
    ).get_attribute("style")

    element: WebElement = driver.find_element(
        By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]'
    )

    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(element, -419, 318).perform()

    after_dragabble: str = driver.find_element(
        By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]'
    ).get_attribute("style")

    assert previous_dragabble != after_dragabble


def test_undraggable_debugger(driver: WebElement):
    driver.maximize_window()
    driver.get(MAIN_PAGE)

    driver.find_element(By.CSS_SELECTOR, ".ant-menu-item").click()

    if (
        len(
            driver.find_elements(
                By.XPATH,
                r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]',
            )
        )
        != 1
    ):
        assert False

    previous_dragabble: str = driver.find_element(
        By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]'
    ).get_attribute("style")

    debugger: WebElement = driver.find_element(
        By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]'
    )
    debugger.find_element(
        By.CSS_SELECTOR, ".ant-btn.ant-btn-primary.ant-btn-dangerous"
    ).click()

    element: WebElement = driver.find_element(
        By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]'
    )

    actions = ActionChains(driver)
    actions.move_to_element_with_offset(element, -419, 318).perform()

    after_dragabble: str = driver.find_element(
        By.XPATH, r'.//*[contains(@class,"GraphStoreDebugger__DemoGraphViewerRoot")]'
    ).get_attribute("style")

    assert previous_dragabble == after_dragabble
