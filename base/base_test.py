import allure
import pytest

from base.base_page import BasePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.menu_page import MenuMod
from pages.cart_page import CartPage
from pages.filter_page import FilterMod
from pages.item_page import ItemPage
from pages.order_page import OrderPage
from pages.about_page import AboutPage

from data.locators import URLs, AuthData, AuthLocs, MenuLocs
from utilities.logger import Logger


class BaseTest:
    # all pages initialization:
    logger: Logger
    log_page: LoginPage
    inv_page: InventoryPage
    menu_page: MenuMod
    cart_page: CartPage
    filter_page: FilterMod
    item_page: ItemPage
    order_page: OrderPage
    about_page: AboutPage

    @pytest.fixture(scope='function', autouse=True)
    def pages_init(self, request, driver):
        Logger.add_start_step('pages_init')
        request.cls.logger = Logger()
        request.cls.log_page = LoginPage(driver, URLs.base_url)
        request.cls.inv_page = InventoryPage(driver, URLs.inventory_url)
        request.cls.menu_page = MenuMod(driver, URLs.base_url)
        request.cls.filter_page = FilterMod(driver, URLs.login_url)
        request.cls.cart_page = CartPage(driver, URLs.cart_url)
        request.cls.item_page = ItemPage(driver, URLs.login_url)
        request.cls.order_page = OrderPage(driver, URLs.checkout_url)
        request.cls.about_page = AboutPage(driver, URLs.about_url)
        Logger.add_end_step(URLs.base_url, 'pages_init')

    # methods:
    @pytest.fixture()
    def fake(self):
        Logger.add_start_step('fake')
        from faker import Faker
        fake = Faker()
        return fake

    @staticmethod
    def rand_num(num) -> int:
        Logger.add_end_step(URLs.base_url, 'rand_num')
        import random
        with allure.step('create a random number based on the page items length...'):
            num = random.randint(0, num - 1)
            return num

    @pytest.fixture()
    def in_out(self, driver):
        Logger.add_end_step(URLs.base_url, 'in_out')
        page = BasePage(driver, URLs.base_url)
        page.open()
        page.screenshot('in_out_0')
        page.is_visible(AuthLocs.input_user).send_keys(AuthData.standard_user)
        page.is_visible(AuthLocs.input_pass).send_keys(AuthData.pass_word)
        page.is_clickable(AuthLocs.login_btn).click()
        page.screenshot('in_out_1')
        print(f'\nlogin...')

        yield

        page.find_el(MenuLocs.menu_btn).click()
        page.is_clickable(MenuLocs.logout_btn).click()
        page.screenshot('in_out_2')
        print(f'\nlogout...')
        Logger.add_end_step(URLs.base_url, 'in_out')
