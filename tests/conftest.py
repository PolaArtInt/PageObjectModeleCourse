import os
import pytest
import allure

from selenium import webdriver
from allure_commons.types import AttachmentType

from utilities.logger import Logger


@pytest.fixture(scope="function", autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    # ignore terminal data:
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    options.add_argument("--headless")

    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--window-size=1280,1000")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)

    yield driver

    # full screenshot in headless mode only (works with screenshot method from base_page):
    s = lambda x: driver.execute_script('return document.body.parentNode.scroll' + x)
    driver.set_window_size(s('Width'), s('Height'))

    # screenshot for allure results (not full screenshot):
    allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)

    driver.quit()


@pytest.fixture()
def logger(driver):
    test_name = os.environ.get('PYTEST_CURRENT_TEST')
    Logger.add_start_step(test_name)
    yield
    Logger.add_end_step(driver.current_url, test_name)
