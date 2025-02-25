import pytest
import allure

from base.base_test import BaseTest
from data.locators import URLs


class TestCart(BaseTest):
    @allure.id('2.1')
    @allure.epic('Cart module')
    @allure.feature('Cart')
    @allure.title('Add items to a cart')
    @pytest.mark.positive
    def test_add_to_cart(self, driver, logger):
        self.log_page.login('standard_user')

        with allure.step('pick the item text and add the item to a cart...'):
            item_titles = self.inv_page.item_names()
            pick_num = self.rand_num(len(item_titles))
            item_title = self.inv_page.item_names()[pick_num].text
            self.inv_page.add_btns()[pick_num].click()
            self.inv_page.screenshot('2.1_test_add_to_cart_1')

        with allure.step('check if the items quantity in the cart is equal to 1...'):
            tag = self.cart_page.cart_tag().text
            assert int(tag) == 1, 'Wrong items quantity in cart'

        with allure.step('go to the cart...'):
            self.cart_page.cart_btn().click()
            self.cart_page.screenshot('2.1_test_add_to_cart_2')

        with allure.step('check if the item picked is the same item in the cart...'):
            cart_item_title = self.inv_page.item_name().text
            assert item_title == cart_item_title, 'A different item was picked'

        with allure.step('remove the item from the cart...'):
            self.cart_page.cart_remove_btn().click()
            self.inv_page.screenshot('2.1_test_add_to_cart_3')

        with allure.step('check if the cart is empty...'):
            assert len(self.inv_page.item_names()) == 0, 'The cart is not empty'

    @allure.id('2.2')
    @allure.epic('Cart module')
    @allure.feature('Cart')
    @allure.title('Remove items from a cart')
    @pytest.mark.positive
    def test_remove_from_cart(self, driver, logger):
        self.log_page.login('standard_user')

        with allure.step('pick 3 items and add them to the cart...'):
            btns_list = self.inv_page.add_btns()
            pick_num = self.rand_num(len(btns_list))
            self.inv_page.add_btns()[pick_num].click()
            self.inv_page.add_btns()[pick_num].click()
            self.inv_page.add_btns()[pick_num].click()
            self.inv_page.screenshot('2.2_test_remove_from_cart_1')

        with allure.step('check if the items quantity in the cart is equal to 3...'):
            tag = self.cart_page.cart_tag().text
            assert int(tag) == 3, 'The cart is empty'

        with allure.step('go to the cart...'):
            self.cart_page.cart_btn().click()
            self.cart_page.screenshot('2.2_test_remove_from_cart_2')

        with allure.step('check if the items quantity in the cart is equal to 3...'):
            items_in_cart = self.inv_page.item_names()
            assert len(items_in_cart) == 3, 'The cart is empty'

        with allure.step('remove the items from the cart...'):
            cart_remove_btns = self.cart_page.cart_remove_btns()
            for btn in cart_remove_btns:
                btn.click()
            self.cart_page.screenshot('2.2_test_remove_from_cart_3')

        with allure.step('check if the cart is empty...'):
            items_in_cart = self.inv_page.item_names()
            assert len(items_in_cart) == 0, 'The cart is not empty'
            assert self.cart_page.cart_tag_invisible(), 'The tag is visible, the cart is not empty'

    @allure.id('2.3')
    @allure.epic('Cart module')
    @allure.feature('Cart')
    @allure.title('Add items to a cart from an item card')
    @pytest.mark.positive
    def test_add_item_from_item_card(self, driver, logger):
        self.log_page.login('standard_user')
        self.inv_page.screenshot('2.3_test_add_item_from_item_card_1')

        with allure.step('pick the item text and go to the item card...'):
            item_titles = self.inv_page.item_names()
            pick_num = self.rand_num(len(item_titles))
            item_title = self.inv_page.item_names()[pick_num].text
            self.inv_page.item_names()[pick_num].click()
            self.inv_page.screenshot('2.3_test_add_item_from_item_card_2')

        with allure.step('check if the item title is the same item title...'):
            card_item_title = self.item_page.card_name().text
            assert item_title == card_item_title, 'Wrong item'

        with allure.step('add the item to the cart from the item page...'):
            self.item_page.card_add_btn().click()
            self.item_page.screenshot('2.3_test_add_item_from_item_card_3')

        with allure.step('go to the cart...'):
            self.cart_page.cart_btn().click()
            self.cart_page.screenshot('2.3_test_add_item_from_item_card_4')

        with allure.step('check if the item title is the same item title and the url is the cart url...'):
            cart_item_title = self.inv_page.item_name().text
            assert cart_item_title == card_item_title and self.cart_page.get_url() == URLs.cart_url, \
                'Wrong url or different item'

        with allure.step('remove the item from the cart...'):
            self.cart_page.cart_remove_btn().click()
            self.cart_page.screenshot('2.3_test_add_item_from_item_card_5')

    @allure.id('2.4')
    @allure.epic('Cart module')
    @allure.feature('Cart')
    @allure.title('Remove items from a cart from an item card')
    @pytest.mark.positive
    def test_remove_item_from_item_card(self, driver, logger):
        self.log_page.login('standard_user')
        self.log_page.screenshot('2.4_test_remove_item_from_item_card_1')

        with allure.step('pick the item text and add the item to the cart...'):
            item_titles = self.inv_page.item_names()
            pick_num = self.rand_num(len(item_titles))
            item_title_before = self.inv_page.item_names()[pick_num].text
            self.inv_page.add_btns()[pick_num].click()
            self.inv_page.screenshot('2.4_test_remove_item_from_item_card_2')

        with allure.step('check if the items quantity in the cart is equal to 1...'):
            tag = self.cart_page.cart_tag()
            assert int(tag.text) == 1, 'Wrong quantity of items'

        with allure.step('go to the cart...'):
            self.inv_page.item_names()[pick_num].click()
            self.inv_page.screenshot('2.4_test_remove_item_from_item_card_3')

        with allure.step('check the item title in the card...'):
            item_title_after = self.item_page.card_name().text
            assert item_title_before == item_title_after, 'Wrong item title'

        with allure.step('click the remove button...'):
            self.item_page.card_remove_btn().click()

        with allure.step('check if the button text is changed...'):
            btn_txt = self.item_page.card_add_btn().text
            assert btn_txt == 'ADD TO CART', 'The button text is not changed'

        with allure.step('check if the cart is empty...'):
            items_in_cart = self.inv_page.item_names()
            assert len(items_in_cart) == 0, 'The cart is not empty'

        with allure.step('check if the cart tag is not presenting on the page...'):
            assert self.cart_page.cart_tag_invisible(), 'The tag is visible, the cart is not empty'
            self.cart_page.screenshot('2.4_test_remove_item_from_item_card_4')
