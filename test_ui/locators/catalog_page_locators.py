from selenium.webdriver.common.by import By


BT_PC_AND_NETWORKS = By.XPATH, '//span[contains(text(), "Компьютеры и сети")]'
BT_LAPTOP_AND_DESKTOP = By.XPATH, '//*[contains(text(),"Ноутбуки,")]'
BT_HOME_AND_GARDEN = By.XPATH, '//span[contains(text(), "Дом и сад")]'
BT_OFFICE_FURNITURE = By.XPATH, '//*[contains(text(),"Офисная")]'
BT_INPUT_DEVICES = By.XPATH,'//*[contains(text(),"Манипулятор")]'
BT_CHAIRS = By.XPATH, '(//a[contains(@href,"chair")])[1]'
BT_NOTEBOOKS = By.XPATH, '(//a[contains(@href,"notebook")])[1]'
BT_KEYBOARDS = By.XPATH, '(//a[contains(@href,"keyboards")])[1]'
BT_MOUSES = By.XPATH, '(//a[contains(@href,"mouse")])[1]'

FILTER_DROPDOWN_TYPE_OF_NOTEBOOK = By.XPATH, '(//div[@class="input-style__real"])[3]'
CHECKBOX_GAMING = By.XPATH, '//div[@class="dropdown-style__checkbox-text"]/div[contains(text(), "игровой")]'
CHECKBOX_GAMING_SINGLE = By.XPATH, '//div[@class="catalog-form__checkbox-text"]/div[contains(text(), "игров")]'

FILTER_DROPDOWN_CPU = By.XPATH, '(//div[@class="input-style__real"])[4]'
CHECKBOX_INTEL_CORE_I9 = By.XPATH, '//div[@class="dropdown-style__checkbox-text"]/div[contains(text(), "Core i9")]'

LINK_FIRST_ITEM = By.XPATH, '(//a[contains(@class, "catalog-form__link_nodecor")])[5]'

SORTER_SELECTION = By.XPATH, "(//select[@class='input-style__real'])[13]"
VALUE_NEW_SORT = By.XPATH, "//option[@value='date:desc']"


