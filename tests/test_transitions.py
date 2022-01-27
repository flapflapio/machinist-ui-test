from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

MAIN_PAGE = "https://machinist.flapflap.io/"
TRANSITION_RING = r'.//*[contains(@class,"TransitionCreatorRing__Ball")]'
NODE_MENU = r'.//*[starts-with(@class,"NodeMenu__NodeMenuRoot")]'


# check if a transition line is present didnt directly use XPATH because with we might end up shifting the order of the SVG elememts
def checking_number_of_transitions(svg_transition_lines: WebElement) -> int:
    numerber_of_transitions = 0 
    for element in svg_transition_lines:
        if len(element.find_elements(By.TAG_NAME, "g")) == 0:
            continue
        else:
            for second_element in element.find_elements(By.TAG_NAME, "g"):
                if (
                    len(second_element.find_elements(By.TAG_NAME, "line")) == 0
                    or len(second_element.find_elements(By.TAG_NAME, "circle")) == 0
                ):
                    continue
                else:
                    assert (
                        len(second_element.find_elements(By.TAG_NAME, "line")) == 1
                        and len(second_element.find_elements(By.TAG_NAME, "circle"))
                        == 1
                    )
                    numerber_of_transitions = numerber_of_transitions + 1

    return numerber_of_transitions


def test_transitioning_nodes(driver: WebDriver):

    driver.maximize_window()
    driver.get(MAIN_PAGE)

    actions = ActionChains(driver)

    canvas_element = driver.find_element(
        By.XPATH, r'.//*[contains(@class,"NodeLayer__Root")]'
    )

    # creating 2 node at distinct locations
    actions.move_to_element_with_offset(
        canvas_element, 350, 350
    ).double_click().perform()

    actions.move_to_element_with_offset(
        canvas_element, 450, 450
    ).double_click().perform()

    nodes = driver.find_elements(By.XPATH, r'.//*[contains(@class,"State__StateRoot")]')

    source_node = nodes[0].find_element(
        By.XPATH, TRANSITION_RING
    )

    target_node = nodes[1].find_element(
        By.XPATH, TRANSITION_RING
    )

    actions.click(nodes[0]).drag_and_drop(source_node, target_node).perform()

    # svg_transition_lines = driver.find_elements(By.TAG_NAME, "svg")
    numerber_of_transitions = checking_number_of_transitions(driver.find_elements(By.TAG_NAME, "svg"))

    # TODO: when change the transitions cercles to arrows neede to modify the cercle to arrows as tag name
    assert numerber_of_transitions == 1

    # second way to check if the tansitions is there is to go check in the node menu if hte transitions is there
    nodes[0].click()

    transition = (
        driver.find_element(
            By.XPATH, NODE_MENU
        )
        .find_element(
            By.XPATH, r'.//*[contains(@class,"NodeMenu__EditableTransitionRoot")]'
        )
        .find_element(By.TAG_NAME, "span")
        .text
    )

    assert transition == "q0 → q1"


def test_two_way_transition(driver: WebDriver):

    driver.maximize_window()
    driver.get(MAIN_PAGE)

    actions = ActionChains(driver)

    canvas_element = driver.find_element(
        By.XPATH, r'.//*[contains(@class,"NodeLayer__Root")]'
    )

    # creating 2 node
    actions.move_to_element_with_offset(
        canvas_element, 200, 200
    ).double_click().perform()

    actions.move_to_element_with_offset(
        canvas_element, 400, 400
    ).double_click().perform()

    nodes = driver.find_elements(By.XPATH, r'.//*[contains(@class,"State__StateRoot")]')

    source_node = nodes[0].find_element(
        By.XPATH, TRANSITION_RING
    )

    target_node = nodes[1].find_element(
        By.XPATH, TRANSITION_RING
    )

    actions.click(nodes[0]).drag_and_drop(source_node, target_node).perform()

    source_node = nodes[1].find_element(
        By.XPATH, TRANSITION_RING
    )

    target_node = nodes[0].find_element(
        By.XPATH, TRANSITION_RING
    )

    actions.click(nodes[1]).drag_and_drop(source_node, target_node).perform()

    #svg_transition_lines = driver.find_elements(By.TAG_NAME, "svg")
    number_of_transaction_lines = checking_number_of_transitions(driver.find_elements(By.TAG_NAME, "svg"))

    # make sure that only 3 transition lines were created
    assert number_of_transaction_lines == 2

    # second way to check if the tansitions is there is to go check in the node menu if hte transitions is there
    nodes[0].click()

    transition = driver.find_element(
        By.XPATH, NODE_MENU
    ).find_elements(
        By.XPATH, r'.//*[contains(@class,"NodeMenu__EditableTransitionRoot")]'
    )

    assert (
        transition[0].find_element(By.TAG_NAME, "span").text == "q0 → q1"
        and transition[1].find_element(By.TAG_NAME, "span").text == "q1 → q0"
    )

    nodes[1].click()

    transition = driver.find_element(
        By.XPATH, NODE_MENU
    ).find_elements(
        By.XPATH, r'.//*[contains(@class,"NodeMenu__EditableTransitionRoot")]'
    )

    assert (
        transition[0].find_element(By.TAG_NAME, "span").text == "q0 → q1"
        and transition[1].find_element(By.TAG_NAME, "span").text == "q1 → q0"
    )


def test_transitioning_three_nodes(driver: WebDriver):

    driver.maximize_window()
    driver.get(MAIN_PAGE)

    actions = ActionChains(driver)

    canvas_element = driver.find_element(
        By.XPATH, r'.//*[contains(@class,"NodeLayer__Root")]'
    )

    # creating 3 node at distinct locations
    actions.move_to_element_with_offset(
        canvas_element, 300, 300
    ).double_click().perform()

    actions.move_to_element_with_offset(
        canvas_element, 500, 500
    ).double_click().perform()

    actions.move_to_element_with_offset(
        canvas_element, 500, 300
    ).double_click().perform()

    nodes = driver.find_elements(By.XPATH, r'.//*[contains(@class,"State__StateRoot")]')

    source_node = nodes[0].find_element(
        By.XPATH, TRANSITION_RING
    )

    target_node = nodes[1].find_element(
        By.XPATH, TRANSITION_RING
    )

    actions.click(nodes[0]).drag_and_drop(source_node, target_node).perform()

    source_node = nodes[1].find_element(
        By.XPATH, TRANSITION_RING
    )

    target_node = nodes[2].find_element(
        By.XPATH, TRANSITION_RING
    )

    actions.click(nodes[1]).drag_and_drop(source_node, target_node).perform()

    source_node = nodes[2].find_element(
        By.XPATH, TRANSITION_RING
    )

    target_node = nodes[0].find_element(
        By.XPATH, TRANSITION_RING
    )

    actions.click(nodes[2]).drag_and_drop(source_node, target_node).perform()
    number_of_transaction_lines = checking_number_of_transitions(driver.find_elements(By.TAG_NAME, "svg"))

    # make sure that only 3 transition lines were created
    assert number_of_transaction_lines == 3

    # second way to check if the tansitions is there is to go check in the node menu if hte transitions is there
    nodes[0].click()

    transition = driver.find_element(
        By.XPATH, NODE_MENU
    ).find_elements(
        By.XPATH, r'.//*[contains(@class,"NodeMenu__EditableTransitionRoot")]'
    )

    assert (
        transition[0].find_element(By.TAG_NAME, "span").text == "q0 → q1"
        and transition[1].find_element(By.TAG_NAME, "span").text == "q2 → q0"
    )

    nodes[1].click()

    transition = driver.find_element(
        By.XPATH, NODE_MENU
    ).find_elements(
        By.XPATH, r'.//*[contains(@class,"NodeMenu__EditableTransitionRoot")]'
    )

    assert (
        transition[0].find_element(By.TAG_NAME, "span").text == "q0 → q1"
        and transition[1].find_element(By.TAG_NAME, "span").text == "q1 → q2"
    )

    nodes[2].click()

    transition = driver.find_element(
        By.XPATH, NODE_MENU
    ).find_elements(
        By.XPATH, r'.//*[contains(@class,"NodeMenu__EditableTransitionRoot")]'
    )

    assert (
        transition[0].find_element(By.TAG_NAME, "span").text == "q1 → q2"
        and transition[1].find_element(By.TAG_NAME, "span").text == "q2 → q0"
    )
