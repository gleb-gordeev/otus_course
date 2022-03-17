from page_objects.RegisterPage import RegisterPage
import helpers

url = "https://demo.opencart.com/index.php?route=account/register"


def test_register(browser):
    browser.get(url)
    string = helpers.random_string()
    email = helpers.random_email()
    phone = helpers.random_phone()
    RegisterPage(browser).fill_register_page(string, string, string, email, phone)
    RegisterPage(browser).check_account(string, string, email, phone)


def test_header(browser):
    browser.get(url)
    RegisterPage(browser).check_header()


def test_help_text(browser):
    browser.get(url)
    RegisterPage(browser).check_help_text()


def test_first_name(browser):
    browser.get(url)
    RegisterPage(browser).check_first_name()


def test_last_name(browser):
    browser.get(url)
    RegisterPage(browser).check_last_name()


def test_email(browser):
    browser.get(url)
    RegisterPage(browser).check_email()
