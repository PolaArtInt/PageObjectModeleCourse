from base.base_page import BasePage
from data.locators import OrderLocs


class OrderPage(BasePage):
    # getters:
    def input_fname(self):
        return self.is_visible(OrderLocs.input_fname)

    def input_lname(self):
        return self.is_visible(OrderLocs.input_lname)

    def input_zipcode(self):
        return self.is_visible(OrderLocs.input_zipcode)

    def checkout_btn(self):
        return self.is_clickable(OrderLocs.checkout_btn)

    def continue_btn(self):
        return self.is_clickable(OrderLocs.continue_btn)

    def finish_btn(self):
        return self.is_clickable(OrderLocs.finish_btn)

    def cancel_btn(self):
        return self.is_clickable(OrderLocs.cancel_btn)

    # methods:
    @staticmethod
    def complete_msg():
        return OrderLocs.complete_msg
