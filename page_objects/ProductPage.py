from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1:nth-child(2)")
    PRICE = (By.CSS_SELECTOR, "ul.list-unstyled>li>h2")
    PROCESSOR_DESCRIPTION = (By.CSS_SELECTOR, "p:nth-child(2)")
    MEMORY_DESCRIPTION = (By.CSS_SELECTOR, "p:nth-child(4)")
    CASE_DESCRIPTION = (By.CSS_SELECTOR, "p:nth-child(6)")

    def check_product_name(self):
        self._element(self.PRODUCT_NAME)

    def check_price(self):
        self._element(self.PRICE)

    def check_processor_description(self):
        self._element(self.PROCESSOR_DESCRIPTION)

    def check_memory_description(self):
        self._element(self.MEMORY_DESCRIPTION)

    def check_case_description(self):
        self._element(self.CASE_DESCRIPTION)
