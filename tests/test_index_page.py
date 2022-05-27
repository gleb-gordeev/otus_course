import allure

from page_objects.IndexPage import IndexPage


@allure.epic("2021Q3")
@allure.feature("Authorization")
@allure.story("Valid credentials")
def test_currency(browser):
    IndexPage(browser).change_currency()


@allure.epic("2021Q3")
@allure.feature("Authorization")
@allure.story("Invalid credentials")
def test_header(browser):
    IndexPage(browser).check_header()


@allure.epic("2022Q4")
@allure.feature("URL check")
@allure.story("URL")
def test_products_list(browser):
    assert len(IndexPage(browser).check_products_list()) == 4


@allure.epic("2022Q4")
@allure.feature("Add button")
@allure.story("Button")
def test_cart_add_button(browser):
    IndexPage(browser).check_cart_add_button()


@allure.epic("2022Q4")
@allure.feature("Wish list")
@allure.story("Button")
def test_wish_list_button(browser):
    IndexPage(browser).check_wish_list_button()


@allure.epic("2022Q4")
@allure.feature("Compare")
@allure.story("Button")
def test_compare_button(browser):
    IndexPage(browser).check_compare_button()
