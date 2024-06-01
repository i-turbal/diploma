import allure

from test_ui.locators.item_page_locators import MARK_CPU_VALUE, MARK_OTHERS_VALUE, TXT_FIRS_PRICE, BT_ADD_FIRST_TO_CART, \
    BT_CONTINUE_SHOPPING, BT_GO_TO_CART
from test_ui.pages.base_page import BasePage


class ItemPage(BasePage):

    def get_cpu_text(self):
        with allure.step("Find and save text of CPU value"):
            return self.driver.find_element(*MARK_CPU_VALUE).text

    def get_others_marks_text(self):
        with allure.step("Find and save text of all other marks"):
            return self.driver.find_element(*MARK_OTHERS_VALUE).text

    def get_first_price(self):
        with allure.step("Find and save first price"):
            return self.wait_for(TXT_FIRS_PRICE).text

    def click_add_to_cart(self):
        with allure.step("Click 'Добавить корзину' of first shop"):
            self.click(BT_ADD_FIRST_TO_CART)

    def click_stay_in_shopping(self):
        with allure.step("Click 'Продолжить покупки' button"):
            self.click(BT_CONTINUE_SHOPPING)

    def click_go_to_cart(self):
        with allure.step("Click 'Перейти в корзину' button"):
            self.wait_for(BT_GO_TO_CART).click()
