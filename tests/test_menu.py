import pytest
import allure

from base.base_test import BaseTest
from data.locators import URLs


class TestMenu(BaseTest):
    @allure.id('6.0')
    @allure.epic('Menu module')
    @allure.feature('Menu')
    @allure.title('Hovering over the menu container')
    @pytest.mark.positive
    def test_hover_on_menu_and_close(self, driver, logger):
        self.log_page.login('standard_user')
        driver.maximize_window()
        self.log_page.screenshot('6.0_test_hover_on_menu_and_close_1')

        with allure.step('click the menu button and hover on the menu box...'):
            self.menu_page.menu_btn().click()
            self.menu_page.screenshot('6.0_test_hover_on_menu_and_close_2')
            self.menu_page.hover(self.menu_page.menu_box())
            self.menu_page.screenshot('6.0_test_hover_on_menu_and_close_3')

        with allure.step('click the x button...'):
            self.menu_page.x_btn().click()

    @allure.id('6.1')
    @allure.epic('Menu module')
    @allure.feature('Menu')
    @allure.title('Checking the logout')
    @pytest.mark.positive
    def test_positive_logout(self, driver, logger):
        self.log_page.login('standard_user')
        self.log_page.screenshot('6.1_test_positive_logout_1')

        # with allure.step('find and click the burger menu...'):
        #     self.menu_page.menu_btn().click()
        #
        # with allure.step('find and click the logout button...'):
        #     self.menu_page.logout_btn().click()
        # or:

        self.menu_page.logout()
        self.menu_page.screenshot('6.1_test_positive_logout_2')

        with allure.step('check if we are on the login page and the login button appears...'):
            assert self.log_page.get_url() == URLs.login_url, 'Wrong url'

            log_btn = self.log_page.login_btn()
            assert self.log_page.login_btn(), 'The login button not appearing'
            assert log_btn.get_attribute('value') == 'LOGIN', 'The login button is not found'

    @allure.id('6.2')
    @allure.epic('Menu module')
    @allure.feature('Menu')
    @allure.title('Checking the about button clickability')
    @pytest.mark.positive
    def test_positive_about_btn(self, driver, logger):
        self.log_page.login('standard_user')
        self.log_page.screenshot('6.2_test_positive_about_btn_1')

        with allure.step('find and click the burger menu...'):
            self.menu_page.menu_btn().click()
            self.menu_page.screenshot('6.2_test_positive_about_btn_2')

        with allure.step('find and click the about button...'):
            self.menu_page.about_btn().click()
            self.menu_page.screenshot('6.2_test_positive_about_btn_3')

        with allure.step('check the expected url and the title...'):
            curr_title = driver.title
            assert self.about_page.get_url() == URLs.about_url and \
                   curr_title == self.about_page.exp_title(), 'Wrong page url or title'

    @allure.id('6.3')
    @allure.epic('Menu module')
    @allure.feature('Menu')
    @allure.title('Checking the reset button')
    @pytest.mark.defect
    @pytest.mark.positive
    def test_reset_app_state_positive(self, driver, logger):
        self.log_page.login('standard_user')
        self.log_page.screenshot('6.3_test_reset_app_state_positive_1')

        with allure.step('add 2 items to the cart...'):
            btns_list = self.inv_page.add_btns()
            pick_num = self.rand_num(len(btns_list))
            self.inv_page.add_btns()[pick_num].click()
            self.inv_page.add_btns()[pick_num].click()
            self.inv_page.screenshot('6.3_test_reset_app_state_positive_2')

        with allure.step('check if the cart quantity tag shows 2...'):
            tag = self.cart_page.cart_tag()
            assert int(tag.text) == 2, 'Wrong items quantity in the cart'

        with allure.step('find and click the burger menu...'):
            self.menu_page.menu_btn().click()
            self.menu_page.screenshot('6.3_test_reset_app_state_positive_3')

        with allure.step('find and click the reset app state button...'):
            self.menu_page.reset_btn().click()
            self.menu_page.screenshot('6.3_test_reset_app_state_positive_4')

        with allure.step('check if the cart is empty...'):
            assert self.cart_page.cart_tag_invisible(), 'The tag is visible, the cart is not empty'

        with allure.step('check if the items quantity in the cart is equal to 0...'):
            try:
                assert len(self.inv_page.item_names()) == 0, 'The cart is not empty'
            except AssertionError:
                print(f'The cart is not empty. There are {len(self.inv_page.item_names())} items in it')

        self.cart_page.refresh()
        self.cart_page.screenshot('6.3_test_reset_app_state_positive_5')

    @allure.id('6.4')
    @allure.epic('Menu module')
    @allure.feature('Menu')
    @allure.title('Checking an app state after clicking on a reset button')
    @pytest.mark.defect
    @pytest.mark.negative
    def test_reset_app_state_negative(self, driver, logger):
        self.log_page.login('standard_user')
        self.log_page.screenshot('6.4_test_reset_app_state_negative_1')

        with allure.step('check the add to cart buttons quantity before...'):
            add_btns_before = self.inv_page.add_btns()

        with allure.step('add 2 items to the cart...'):
            btns_list = self.inv_page.add_btns()
            pick_num = self.rand_num(len(btns_list))
            self.inv_page.add_btns()[pick_num].click()
            self.inv_page.add_btns()[pick_num].click()
            self.inv_page.screenshot('6.4_test_reset_app_state_negative_2')

        with allure.step('check the items quantity in the cart is equal to 2...'):
            tag = self.cart_page.cart_tag()
            assert int(tag.text) == 2, 'Wrong items quantity in the cart'

        with allure.step('find and click the burger menu...'):
            self.menu_page.menu_btn().click()
            self.menu_page.screenshot('6.4_test_reset_app_state_negative_3')

        with allure.step('find and click the reset app state button...'):
            self.menu_page.reset_btn().click()
            self.menu_page.screenshot('6.4_test_reset_app_state_negative_4')

        with allure.step('check if the cart is empty...'):
            assert self.cart_page.cart_tag_invisible(), 'The tag is visible, the cart is not empty'

        with allure.step('check there are no items in the cart...'):
            items_in_cart = self.cart_page.cart_remove_btns()
            assert len(items_in_cart) == 0, f'There are {len(items_in_cart)} items in a cart'

        with allure.step('check there are all add to cart buttons are unpressed by its quantity before and after...'):
            add_btns_after = self.inv_page.add_btns()

            try:
                assert len(add_btns_before) == len(add_btns_after), 'The buttons are not unpressed after reset the app'
            except AssertionError:
                print(f'\nThere are {len(add_btns_after)} "ADD TO CART" buttons instead of {len(add_btns_before)}')
                print(f'\nThe buttons are not unpressed after reset the app')

        self.cart_page.refresh()
        self.cart_page.screenshot('6.4_test_reset_app_state_negative_5')
