from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class IndexPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "h1>a")
    CART_ADD_BUTTON = (By.CSS_SELECTOR, "div.button-group>button:nth-child(1)")
    WISH_LIST_BUTTON = (By.CSS_SELECTOR, "div.button-group>button:nth-child(2)")
    COMPARE_BUTTON = (By.CSS_SELECTOR, "div.button-group>button:nth-child(3)")
    PRODUCTS_LIST = (By.CSS_SELECTOR, "div.product-layout")
    CURRENCY = (By.CSS_SELECTOR, ".btn.btn-link.dropdown-toggle")
    CURRENT_CURRENCY = (By.CSS_SELECTOR, ".btn>strong")
    EURO = (By.CSS_SELECTOR, "[name='EUR']")
    USD = (By.CSS_SELECTOR, "[name='USD']")

    def check_header(self):
        self._element(self.HEADER)

    def check_cart_add_button(self):
        self._element(self.CART_ADD_BUTTON)

    def check_wish_list_button(self):
        self._element(self.WISH_LIST_BUTTON)

    def check_compare_button(self):
        self._element(self.COMPARE_BUTTON)

    def check_products_list(self):
        all_list = self._elements(self.PRODUCTS_LIST)
        list_elements = [x.text for x in all_list if len(x.text) > 0]
        return list_elements

    def change_currency(self):
        self._click(self.CURRENCY)
        self._click(self.EURO)
        assert self._element(self.CURRENT_CURRENCY).text == "€"
        self._click(self.CURRENCY)
        self._click(self.USD)
        assert self._element(self.CURRENT_CURRENCY).text == "$"
