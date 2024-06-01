from selenium.webdriver.common.by import By

MARK_CPU_VALUE = By.XPATH, '//tbody[2]/tr[3]/td[2]/span[@class="value__text"]'
MARK_OTHERS_VALUE = By.XPATH, '//tbody[15]//tr/td[2]/span[@class="value__text"]'

TXT_FIRS_PRICE = By.XPATH, '(//a[contains(@class, "product-aside__link")]/span)[1]'

BT_ADD_FIRST_TO_CART = By.XPATH, '(//a[contains(text(),"В корзин")])[1]'
BT_CONTINUE_SHOPPING = By.XPATH, '//a[contains(text(),"Продолжить покупки")]'
BT_GO_TO_CART = By.XPATH, '//a[contains(text(),"Перейти в корзину")]'
