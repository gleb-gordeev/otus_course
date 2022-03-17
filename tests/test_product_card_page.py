from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.ProductPage import ProductPage


url = "https://demo.opencart.com/index.php?route=product/product&product_id=43"


def test_product_name(browser):
    browser.get(url)
    ProductPage(browser).check_product_name()


def test_price(browser):
    browser.get(url)
    ProductPage(browser).check_price()


def test_processor_description(browser):
    browser.get(url)
    ProductPage(browser).check_processor_description()


def test_memory_description(browser):
    browser.get(url)
    ProductPage(browser).check_memory_description()


def test_case_description(browser):
    browser.get(url)
    ProductPage(browser).check_case_description()
