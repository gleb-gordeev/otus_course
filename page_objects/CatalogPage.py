from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CatalogPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "div>h2")
    SORT = (By.CSS_SELECTOR, "[for='input-sort']")
    SHOW = (By.CSS_SELECTOR, "[for='input-limit']")
    PRODUCTS_LIST = (By.CSS_SELECTOR, "div.product-layout")
    PRICES_LIST = (By.CSS_SELECTOR, "div>p.price")

    def check_header(self):
        self.is_present(self.HEADER)

    def check_sort(self):
        self.is_present(self.SORT)

    def check_show(self):
        self.is_present(self.SHOW)

    def check_products_list(self):
        all_list = self._elements(self.PRODUCTS_LIST)
        list_elements = [x.text for x in all_list if len(x.text) > 0]
        return list_elements

    def check_prices_list(self):
        all_list = self._elements(self.PRICES_LIST)
        list_elements = [x.text for x in all_list if len(x.text) > 0]
        return list_elements
