from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from page_objects.elements.SuccessAlert import SuccessAlert
from selenium.common.exceptions import NoSuchElementException


class AdminPage(BasePage, SuccessAlert):
    LOGO = (By.CSS_SELECTOR, "#header-logo>a>img")
    HELP_TEXT = (By.CSS_SELECTOR, "h1.panel-title")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "span.help-block")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "span.help-block")
    INPUT_LOGIN = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    CATALOG_BUTTON = (By.CSS_SELECTOR, "#menu-catalog>a")
    CATALOG_PRODUCTS_BUTTON = (By.CSS_SELECTOR, "#menu-catalog>ul>:nth-child(2)")
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, "div.pull-right>:nth-child(2)")
    CATEGORY_NAME = (By.CSS_SELECTOR, "#input-name1")
    DEVICE_DESCRIPTION = (By.CSS_SELECTOR, ".note-editable")
    META_TAG = (By.CSS_SELECTOR, "#input-meta-title1")
    SAVE_DEVICE = (By.CSS_SELECTOR, "button[data-original-title=Save]")
    DATA_TAB = (By.XPATH, "//*[text()='Data']")
    MODEL_NAME = (By.CSS_SELECTOR, "#input-model")
    LAST_PAGE = (By.XPATH, "//*[text()='>|']")
    DEVICE_FOR_DELETE = (By.CSS_SELECTOR, "tbody>tr:nth-child(1)>td>input")
    DEVICE_NAME = (By.CSS_SELECTOR, "tbody>tr>td:nth-child(3)")
    LAST_DEVICE = (By.CSS_SELECTOR, "tbody>tr:last-child>td:nth-child(3)")
    DELETE_BUTTON = (By.CSS_SELECTOR, "div.pull-right>:nth-child(4)")

    def check_logo(self):
        self.is_present(self.LOGO)

    def check_help_text(self):
        self.is_present(self.HELP_TEXT)

    def check_forgot_password(self):
        self.is_present(self.FORGOT_PASSWORD)

    def check_login_button(self):
        self.is_present(self.LOGIN_BUTTON)

    def login_with(self, username, password):
        self.input_and_submit(self.INPUT_LOGIN, username)
        self.input_and_submit(self.INPUT_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def click_catalog(self):
        self.click(self.CATALOG_BUTTON)

    def click_products(self):
        self.click(self.CATALOG_PRODUCTS_BUTTON)

    def click_add_new(self):
        self.click(self.ADD_NEW_BUTTON)

    def new_device_check(self, category, device_desc, tag, model):
        self.is_present(self.CATEGORY_NAME).send_keys(category)
        self.is_present(self.DEVICE_DESCRIPTION).send_keys(device_desc)
        self.is_present(self.META_TAG).send_keys(tag)
        self.is_present(self.DATA_TAB).click()
        self.is_present(self.MODEL_NAME).send_keys(model)
        self.is_present(self.SAVE_DEVICE)

    def delete_device(self):
        self.click(self.DEVICE_FOR_DELETE)
        self.click(self.DELETE_BUTTON)
        SuccessAlert(self.browser).alert_confirm()

    def first_device(self):
        return self.is_present(self.DEVICE_NAME).text

    def last_device(self):
        return self.is_present(self.LAST_DEVICE).text

    def last_page(self):
        return self.click(self.LAST_PAGE)

    def search_element(self, r_device_name):
        try:
            search_device = self.is_present((By.XPATH, f"//*[text()='{r_device_name}']")).text
        except NoSuchElementException:
            self.last_page()
            search_device = self.is_present((By.XPATH, f"//*[text()='{r_device_name}']")).text
        return search_device
