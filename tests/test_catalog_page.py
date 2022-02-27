from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.CatalogPage import CatalogPage

url = "https://demo.opencart.com/index.php?route=product/category&path=20"


def test_header(browser):
    browser.get(url)
    CatalogPage(browser).check_header()


def test_sort(browser):
    browser.get(url)
    CatalogPage(browser).check_sort()


def test_show(browser):
    browser.get(url)
    CatalogPage(browser).check_show()


def test_products_list(browser):
    browser.get(url)
    assert len(CatalogPage(browser).check_products_list()) == 12


def test_prices_list(browser):
    browser.get(url)
    assert len(CatalogPage(browser).check_prices_list()) == 12
