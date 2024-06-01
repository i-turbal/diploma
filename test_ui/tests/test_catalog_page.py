import time

import allure
import pytest

from test_ui.pages.cart_page import CartPage, find_price_in_string
from test_ui.pages.catalog_page import CatalogPage
from test_ui.pages.item_page import ItemPage
from test_ui.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def item_page(driver):
    yield ItemPage(driver)


@pytest.fixture(autouse=True)
def catalog_page(driver):
    yield CatalogPage(driver)


@pytest.fixture(autouse=True)
def cart_page(driver):
    yield CartPage(driver)


class TestCatalogPage:

    @pytest.mark.catalog
    @pytest.mark.filters
    @pytest.mark.regress
    @allure.title("Test adding filters")
    @allure.description("This test adds two filters and checks selected filters on Item page")
    @allure.feature("Filters")
    @allure.suite("Tests of catalog")
    def test_add_filters(self, main_page, catalog_page, item_page):
        main_page.click_button_catalog()
        catalog_page.click_pc_and_networks()
        catalog_page.go_to_notebooks()
        catalog_page.open_dropdown_type_notebook()
        gaming_type_filter = catalog_page.get_text_of_gaming_checkbox()
        catalog_page.select_gaming_checkbox()
        catalog_page.open_cpu_dropdown_filter()
        intel_core_i9_filter = catalog_page.get_text_of_intel_core_i9_checkbox()
        catalog_page.select_intel_core_i9()
        catalog_page.sort_list_by_new()
        catalog_page.open_first_item()
        cpu_on_item_page = item_page.get_cpu_text()
        other_marks_text = item_page.get_others_marks_text()
        with allure.step("Compare added filters on the list with marks on item card"):
            assert cpu_on_item_page == intel_core_i9_filter
            assert gaming_type_filter in other_marks_text

    @pytest.mark.catalog
    @pytest.mark.smoke
    @pytest.mark.regress
    @pytest.mark.cart
    @allure.title("Test add more 1 one item to the cart ")
    @allure.description("This test adds 3 items to the cart and check total price ")
    @allure.suite("Test E2E")
    def test_buy_gamer_stuff(self, main_page, catalog_page, item_page, cart_page):
        main_page.click_button_catalog()
        catalog_page.click_home_and_garden()
        catalog_page.go_to_office_chairs()
        catalog_page.select_gaming()
        catalog_page.open_first_item()
        chair_first_price = float(item_page.get_first_price().replace(",", "."))
        item_page.click_add_to_cart()
        item_page.click_stay_in_shopping()
        main_page.click_button_catalog()
        catalog_page.click_pc_and_networks()
        catalog_page.go_to_keyboards()
        catalog_page.select_gaming()
        catalog_page.open_first_item()
        keyboard_first_prise = float(item_page.get_first_price().replace(",", "."))
        item_page.click_add_to_cart()
        main_page.click_button_catalog()
        catalog_page.click_pc_and_networks()
        catalog_page.go_to_mouses()
        catalog_page.select_gaming()
        catalog_page.open_first_item()
        mouse_first_price = float(item_page.get_first_price().replace(",", "."))
        item_page.click_add_to_cart()
        item_page.click_go_to_cart()
        total_price = find_price_in_string(cart_page.get_total_price_string())
        with allure.step("Compare sum of items and total price on the cart"):
            assert total_price == chair_first_price + keyboard_first_prise + mouse_first_price

