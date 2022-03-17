from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects import AdminPage
import helpers
import time
import pytest


url = "http://localhost/opencart/upload/admin/"


def test_add_new_product(browser):
    r_device_name = helpers.random_string()
    browser.get(url)
    AdminPage(browser).login_with("admin", "admin")
    AdminPage(browser).click_catalog()
    AdminPage(browser).click_products()
    AdminPage(browser).click_add_new()
    AdminPage(browser).new_device_check(r_device_name, "test2", "test3", r_device_name)
    assert AdminPage(browser).search_element(r_device_name) == r_device_name


def test_del_product(browser):
    browser.get(url)
    AdminPage(browser).login_with("admin", "admin")
    AdminPage(browser).click_catalog()
    AdminPage(browser).click_products()
    deleted_device = AdminPage(browser).first_device()
    AdminPage(browser).delete_device()
    new_device = AdminPage(browser).first_device()
    assert new_device != deleted_device


def test_check_header_logo(browser):
    browser.get(url)
    AdminPage(browser).check_logo()


def test_check_help_text(browser):
    browser.get(url)
    AdminPage(browser).check_help_text()


def test_check_forgot_password(browser):
    browser.get(url)
    AdminPage(browser).check_forgot_password()


def test_check_login_button(browser):
    browser.get(url)
    AdminPage(browser).check_login_button()






