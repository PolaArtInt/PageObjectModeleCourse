import allure

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

from utilities.logger import Logger


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = Logger()

    # getters:
    def find_el(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def find_elems(self, locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def is_visible(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located(locator))

    def are_visible(self, locator) -> list[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located(locator))

    def is_invisible(self, locator) -> WebElement:
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def visibility_of(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of(locator))

    def is_clickable(self, locator) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable(locator))

    # actions:
    def open(self):
        Logger.add_start_step('open')
        with allure.step('open the page'):
            self.driver.get(self.url)

    def get_url(self) -> str:
        Logger.add_start_step('get_url')
        with allure.step('get the current page url'):
            print(self.driver.current_url)
            return self.driver.current_url

    def refresh(self):
        Logger.add_start_step('refresh')
        with allure.step('refresh the page'):
            self.driver.refresh()

    def hover(self, elem: WebElement):
        Logger.add_start_step('hover')
        with allure.step('hold mouse on the element'):
            return ActionChains(self.driver).move_to_element(elem).pause(5)

    # methods:
    def screenshot(self, test_name):
        Logger.add_start_step('screenshot')
        with allure.step('take full screenshot in headless mode...'):
            self.driver.find_element('tag name', 'body').screenshot(f'..\\screenshots\\{test_name}.png')
