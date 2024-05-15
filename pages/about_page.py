from base.base_page import BasePage
from data.locators import AboutLocs


class AboutPage(BasePage):
    # methods:
    @staticmethod
    def exp_title():
        return AboutLocs.exp_title
