import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from test_ui.locators.cart_page_locators import TXT_TOTAL_PRICE
from test_ui.pages.base_page import BasePage


def find_price_in_string(price_str: str):
    str_price = price_str.split(":")[1].split()[0]
    int_price = float(str_price.replace(',', '.'))
    return int_price


class CartPage(BasePage):

    def get_total_price_string(self):
        with allure.step("Find string about how many items we have in the cart and their price"):
            return self.wait_for(TXT_TOTAL_PRICE).text

