from page_objects.AdminPage import AdminPage
import helpers
import allure


url = "http://192.168.1.105:80/admin/"


@allure.title("Local opencart test #1")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_new_product(browser):
    """this test fail without opencart"""
    r_device_name = helpers.random_string()
    browser.get(url)
    AdminPage(browser).login_with("user", "bitnami")
    AdminPage(browser).click_catalog()
    AdminPage(browser).click_products()
    AdminPage(browser).click_add_new()
    AdminPage(browser).new_device_check(r_device_name, "test2", "test3", r_device_name)
    assert AdminPage(browser).search_element(r_device_name) == r_device_name


@allure.title("Local opencart test #2")
@allure.severity(allure.severity_level.CRITICAL)
def test_del_product(browser):
    """this test fail without opencart"""
    browser.get(url)
    AdminPage(browser).login_with("user", "bitnami")
    AdminPage(browser).click_catalog()
    AdminPage(browser).click_products()
    deleted_device = AdminPage(browser).first_device()
    AdminPage(browser).delete_device()
    new_device = AdminPage(browser).first_device()
    assert new_device != deleted_device


@allure.title("Local opencart test #3")
@allure.severity(allure.severity_level.MINOR)
def test_check_header_logo(browser):
    """this test fail without opencart"""
    browser.get(url)
    AdminPage(browser).check_logo()


@allure.title("Local opencart test #4")
@allure.severity(allure.severity_level.MINOR)
def test_check_help_text(browser):
    """this test fail without opencart"""
    browser.get(url)
    AdminPage(browser).check_help_text()


@allure.title("Local opencart test #5")
@allure.severity(allure.severity_level.MINOR)
def test_check_forgot_password(browser):
    """this test fail without opencart"""
    browser.get(url)
    AdminPage(browser).check_forgot_password()


@allure.title("Local opencart test #6")
@allure.severity(allure.severity_level.MINOR)
def test_check_login_button(browser):
    """this test fail without opencart"""
    browser.get(url)
    AdminPage(browser).check_login_button()
