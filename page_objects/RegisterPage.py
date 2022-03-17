from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class RegisterPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "div#content>h1")
    HELP_TEXT = (By.CSS_SELECTOR, "div#content>p")
    FIRST_NAME = (By.CSS_SELECTOR, "[name='firstname']")
    LAST_NAME = (By.CSS_SELECTOR, "[name='lastname']")
    EMAIL = (By.CSS_SELECTOR, "[name='email']")
    PHONE = (By.CSS_SELECTOR, "[name='telephone']")
    PASSWORD = (By.CSS_SELECTOR, "[name='password']")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "[name='confirm']")
    POLICY_CHECKBOX = (By.CSS_SELECTOR, "[name='agree']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[value='Continue']")
    MY_ACCOUNT_MENU = (By.CSS_SELECTOR, "[title='My Account']")
    MY_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".dropdown-menu-right>:nth-child(1)")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".dropdown-menu-right>:nth-child(5)")
    EDIT_ACCOUNT = (By.CSS_SELECTOR, ".list-group>:nth-child(2)")

    def check_header(self):
        self.is_present(self.HEADER)

    def check_help_text(self):
        self.is_present(self.HELP_TEXT)

    def check_first_name(self):
        self.is_present(self.FIRST_NAME)

    def check_last_name(self):
        self.is_present(self.LAST_NAME)

    def check_email(self):
        self.is_present(self.EMAIL)

    def fill_register_page(self, first_name, last_name, password, email, phone):
        self.input_and_submit(self.FIRST_NAME, first_name)
        self.input_and_submit(self.LAST_NAME, last_name)
        self.input_and_submit(self.EMAIL, email)
        self.input_and_submit(self.PHONE, phone)
        self.input_and_submit(self.PASSWORD, password)
        self.input_and_submit(self.PASSWORD_CONFIRM, password)
        self.click(self.POLICY_CHECKBOX)
        self.click(self.CONTINUE_BUTTON)

    def check_account(self, first_name, last_name, email, phone):
        self.click(self.MY_ACCOUNT_MENU)
        self.click(self.MY_ACCOUNT_BUTTON)
        self.click(self.EDIT_ACCOUNT)
        assert self.is_present(self.FIRST_NAME).get_attribute("value") == first_name
        assert self.is_present(self.LAST_NAME).get_attribute("value") == last_name
        assert self.is_present(self.EMAIL).get_attribute("value") == email
        assert self.is_present(self.PHONE).get_attribute("value") == phone

    def logout(self):
        self.click(self.MY_ACCOUNT_MENU)
        self.click(self.LOGOUT_BUTTON)
