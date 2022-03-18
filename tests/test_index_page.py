import allure

from page_objects.IndexPage import IndexPage

url = "https://demo.opencart.com/index.php?"


@allure.epic("2021Q3")
@allure.feature("Authorization")
@allure.story("Valid credentials")
def test_currency(browser):
    browser.get(url)
    IndexPage(browser).change_currency()


@allure.epic("2021Q3")
@allure.feature("Authorization")
@allure.story("Invalid credentials")
def test_header(browser):
    browser.get(url)
    IndexPage(browser).check_header()


@allure.epic("2022Q4")
@allure.feature("URL check")
@allure.story("URL")
def test_products_list(browser):
    browser.get(url)
    assert len(IndexPage(browser).check_products_list()) == 4


@allure.epic("2022Q4")
@allure.feature("Add button")
@allure.story("Button")
def test_cart_add_button(browser):
    browser.get(url)
    IndexPage(browser).check_cart_add_button()


@allure.epic("2022Q4")
@allure.feature("Wish list")
@allure.story("Button")
def test_wish_list_button(browser):
    browser.get(url)
    IndexPage(browser).check_wish_list_button()


@allure.epic("2022Q4")
@allure.feature("Compare")
@allure.story("Button")
def test_compare_button(browser):
    browser.get(url)
    IndexPage(browser).check_compare_button()
