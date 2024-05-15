import allure

from base.base_page import BasePage
from data.locators import MenuLocs


class MenuMod(BasePage):
    # getters:
    def menu_box(self):
        return self.is_visible(MenuLocs.menu_container)

    def menu_btn(self):
        return self.find_el(MenuLocs.menu_btn)

    def all_items_btn(self):
        return self.is_clickable(MenuLocs.all_items_btn)

    def about_btn(self):
        return self.is_clickable(MenuLocs.about_btn)

    def logout_btn(self):
        return self.is_clickable(MenuLocs.logout_btn)

    def reset_btn(self):
        return self.is_clickable(MenuLocs.reset_btn)

    def x_btn(self):
        return self.is_clickable(MenuLocs.x_btn)

    # methods:
    def logout(self):
        with allure.step('logout...'):
            self.menu_btn().click()
            self.logout_btn().click()
