from selenium.webdriver.common.by import By


class SuccessAlert:
    def __init__(self, browser):
        self.browser = browser

    def click_login(self):
        self.browser.find_element(By.CSS_SELECTOR, ".alert-success").find_element(
            By.LINK_TEXT, 'login'
        ).click()

    def click_shopping_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, ".alert-success").find_element(
            By.LINK_TEXT, "shopping cart"
        ).click()

    def click_product_comparison(self):
        self.browser.find_element(By.CSS_SELECTOR, ".alert-success").find_element(
            By.LINK_TEXT, "product comparison"
        ).click()

    def alert_confirm(self):
        confirm_alert = self.browser.switch_to.alert
        confirm_alert.accept()
