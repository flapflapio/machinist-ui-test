from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver


def test_python_dot_org(driver: WebDriver):
    """This is a demo test that shows basic usage of selenium.

    Args:
        driver (WebDriver): The WebDriver test fixture. Injected by pytest.
    """

    driver.get("https://www.python.org")

    # Enter a search
    ele = driver.find_element(By.TAG_NAME, "#id-search-field")
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
