from base.base_page import BasePage
from data.locators import InventoryLocs


class InventoryPage(BasePage):
    # getters:
    def inventory_header(self):
        return self.is_visible(InventoryLocs.prod_header)

    def inventory_cards(self):
        return self.find_elems(InventoryLocs.item_cards)

    def inventory_card(self):
        return self.find_el(InventoryLocs.item_cards)

    def item_imgs(self):
        return self.find_elems(InventoryLocs.item_imgs)

    def item_img(self):
        return self.find_el(InventoryLocs.item_imgs)

    def item_names(self):
        return self.find_elems(InventoryLocs.item_names)

    def item_name(self):
        return self.find_el(InventoryLocs.item_names)

    def item_descs(self):
        return self.find_elems(InventoryLocs.item_descs)

    def item_desc(self):
        return self.find_el(InventoryLocs.item_descs)

    def item_prices(self):
        return self.find_elems(InventoryLocs.item_prices)

    def item_price(self):
        return self.find_el(InventoryLocs.item_prices)

    def add_btns(self):
        return self.are_visible(InventoryLocs.add_btns)

    def add_btn(self):
        return self.find_el(InventoryLocs.add_btns)

    def remove_btns(self):
        return self.find_elems(InventoryLocs.remove_btns)

    def remove_btn(self):
        return self.find_el(InventoryLocs.remove_btns)
