from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

web = "https://machinist.flapflap.io/"


def test_transition_label_presence(driver: WebDriver):
    driver.get(web)

    canvas_element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]')
    action = ActionChains(driver)

    # Adding q0 theoretically even if bug is present
    action.move_to_element_with_offset(
        canvas_element, 100, 100
    ).double_click().perform()

    # Adding q1 theoretically with bug present
    action.move_to_element_with_offset(
        canvas_element, 200, 200
    ).double_click().perform()

    driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div/div[2]').click()

    # The transition ball
    source = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div[1]/div/div[2]/div[2]/div'
    )

    # Drag to q1
    target = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div/div[3]')
    action.click_and_hold(source).drag_and_drop(source, target).perform()

    driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div/div[2]').click()

    # add label to transition
    ele = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/section/div/div[3]/div[2]/div/input'
    )
    ele.send_keys(Keys.TAB)
    ele.clear()
    ele.send_keys("abc")

    output_element = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div[1]/div/p'
    ).text

    assert "abc" == output_element


def test_node_label_present(driver: WebDriver):

    driver.get(web)
    canvas_element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]')
    action = ActionChains(driver)

    # Adding q0 theoretically even if bug is present
    action.move_to_element_with_offset(
        canvas_element, 100, 100
    ).double_click().perform()

    output_element = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div[1]/div/div'
    ).text

    assert output_element == "q0"
