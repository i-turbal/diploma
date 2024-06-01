
import allure
from selenium.webdriver import Keys


from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import StaleElementReferenceException

from test_ui.locators.catalog_page_locators import BT_LAPTOP_AND_DESKTOP, BT_NOTEBOOKS, FILTER_DROPDOWN_CPU, \
    CHECKBOX_INTEL_CORE_I9, FILTER_DROPDOWN_TYPE_OF_NOTEBOOK, CHECKBOX_GAMING, BT_PC_AND_NETWORKS, SORTER_SELECTION, \
    LINK_FIRST_ITEM, BT_HOME_AND_GARDEN, BT_OFFICE_FURNITURE, BT_CHAIRS, CHECKBOX_GAMING_SINGLE, BT_KEYBOARDS, \
    BT_INPUT_DEVICES, BT_MOUSES
from test_ui.pages.base_page import BasePage


class CatalogPage(BasePage):

    @property
    def pc(self):  # find PC section
        return self.wait_for(BT_LAPTOP_AND_DESKTOP)

    @property
    def notebooks(self):  # find notebooks sections
        return self.wait_for(BT_NOTEBOOKS)

    """"Work with filters CPU"""

    @property
    def cpu_dropdown_filter(self):  # find cpu dropdown filter
        return self.driver.find_element(*FILTER_DROPDOWN_CPU)

    @property
    def checkbox_inter_core_i9(self):  #find inter core i9 checkbox
        return self.wait_for(CHECKBOX_INTEL_CORE_I9)

    def open_cpu_dropdown_filter(self):
        with allure.step("Open 'Оперативная память' drop-down filter"):
            self.driver.execute_script('arguments[0].click()', self.cpu_dropdown_filter)

    def get_text_of_intel_core_i9_checkbox(self):
        with allure.step("Save value of Intel core i9 checkbox"):
            return self.checkbox_inter_core_i9.text

    def select_intel_core_i9(self):
        with allure.step("Select intel core i9 checkbox filter"):
            self.driver.execute_script('arguments[0].click()', self.checkbox_inter_core_i9)

    @property
    def notebook_type_dropdown(self):  # find drop-down for select type of notebook
        return self.driver.find_element(*FILTER_DROPDOWN_TYPE_OF_NOTEBOOK)

    #
    @property
    def gaming_notebook_checkbox(self):  # find checkbox in dropdown
        return self.wait_for(CHECKBOX_GAMING)

    def open_dropdown_type_notebook(self):
        with allure.step("Open 'Подобрать в один клик' drop-down filter"):
            self.driver.execute_script('arguments[0].click()', self.notebook_type_dropdown)

    def get_text_of_gaming_checkbox(self):
        with allure.step("Save value 'Игровой' checkbox filter"):
            return self.gaming_notebook_checkbox.text

    def select_gaming_checkbox(self):
        with allure.step('Click the "игровой" checkbox'):
            self.driver.execute_script('arguments[0].click()', self.gaming_notebook_checkbox)

    def click_pc_and_networks(self):
        with allure.step('Go to "Коммьютеры и сети" section'):
            self.click(BT_PC_AND_NETWORKS)

    def go_to_notebooks(self):
        with allure.step("Go to 'Ноутбуки, компьютеры, мониторы' category"):
            action = ActionChains(self.driver)
            action.move_to_element(self.pc).perform()
        with allure.step("Open 'Ноутбуки' sub-categpry"):
            action.move_to_element(self.notebooks).perform()
            action.click().perform()

    """Work with sorter"""

    def sort_list_by_new(self):
        with allure.step("Sort list by 'Новые'"):
            action = ActionChains(self.driver)
            selector = self.driver.find_element(*SORTER_SELECTION)
            action.move_to_element(selector).perform()
            action.click().perform()
            for _ in range(3):
                selector.send_keys(Keys.ARROW_DOWN)
            selector.send_keys(Keys.ENTER)

    """Work with first link"""

    @property
    def first_link(self):
        return self.driver.find_element(*LINK_FIRST_ITEM)

    def open_first_item(self):
        with allure.step('Open first item'):
            try:
                self.click(LINK_FIRST_ITEM)
            except StaleElementReferenceException:
                element = self.driver.find_element(*LINK_FIRST_ITEM)
                element.click()

    def get_text_of_first_item(self):
        return self.first_link.text

    def click_home_and_garden(self):
        with allure.step('Go to "Дом и сад" section'):
            self.click(BT_HOME_AND_GARDEN)

    @property
    def office_furniture(self):
        return self.wait_for(BT_OFFICE_FURNITURE)

    @property
    def office_chairs(self):
        return self.wait_for(BT_CHAIRS)

    def go_to_office_chairs(self):
        with allure.step("Go to 'Офисная мебель' category"):
            action = ActionChains(self.driver)
            action.move_to_element(self.office_furniture).perform()
        with allure.step("Open 'Офисные стулья' sub-categpry"):
            action.move_to_element(self.office_chairs).perform()
            action.click().perform()

    @property
    def gaming_single_checkbox(self):
        return self.driver.find_element(*CHECKBOX_GAMING_SINGLE)

    def select_gaming(self):
        with allure.step("Select 'Игровой/ая' checkbox"):
            self.driver.execute_script('arguments[0].click()', self.gaming_single_checkbox)

    @property
    def keyboards(self):
        return self.wait_for(BT_KEYBOARDS)

    @property
    def input_devices(self):
        return self.wait_for(BT_INPUT_DEVICES)

    @property
    def mouses(self):
        return self.wait_for(BT_MOUSES)

    def go_to_keyboards(self):
        with allure.step("Go to 'Манипуляторы и устройства ввода' category"):
            action = ActionChains(self.driver)
            action.move_to_element(self.input_devices).perform()
        with allure.step("Open 'Клавиатуры' sub-categpry"):
            action.move_to_element(self.keyboards).perform()
            action.click().perform()

    def go_to_mouses(self):
        with allure.step("Go to 'Манипуляторы и устройства ввода' category"):
            action = ActionChains(self.driver)
            action.move_to_element(self.input_devices).perform()
        with allure.step("Open 'Мыши' sub-categpry"):
            action.move_to_element(self.mouses).perform()
            action.click().perform()
