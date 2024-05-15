import allure
import pytest

from base.base_test import BaseTest


class TestExOrder(BaseTest):
    @allure.id('2.1')
    @pytest.mark.positive
    @pytest.mark.run(order=5)
    def test_1(self, driver):
        print('Method 1')

    @allure.id('2.2')
    @pytest.mark.positive
    @pytest.mark.run(order=4)
    def test_2(self, driver):
        print('Method 2')

    @allure.id('2.3')
    @pytest.mark.positive
    @pytest.mark.run(order=2)
    def test_3(self, driver):
        print('Method 3')

    @allure.id('2.4')
    @pytest.mark.positive
    @pytest.mark.run(order=3)
    def test_4(self, driver):
        print('Method 4')

    @allure.id('2.5')
    @pytest.mark.positive
    @pytest.mark.run(order=1)
    def test_5(self, driver):
        print('Method 5')
