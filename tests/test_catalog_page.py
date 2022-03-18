import allure

from page_objects.CatalogPage import CatalogPage

url = "https://demo.opencart.com/index.php?route=product/category&path=20"


@allure.link('https://youtu.be/dQw4w9WgXcQ')
def test_header(browser):
    browser.get(url)
    CatalogPage(browser).check_header()


@allure.title("Test screenshot")
@allure.link('https://youtu.be/dQw4w9WgXcQ', name='Click me')
def test_sort(browser):
    """this test fail for screen test"""
    browser.get(url)
    CatalogPage(browser).check_sort()


@allure.title("Test screenshot")
@allure.issue('1', name='Failed test #1 task link')
def test_show(browser):
    """this test fail for screen test"""
    browser.get(url)
    CatalogPage(browser).check_show()


@allure.testcase('1', 'Test case #1')
def test_products_list(browser):
    browser.get(url)
    assert len(CatalogPage(browser).check_products_list()) == 12


@allure.link('https://coinmarketcap.com/ru/currencies/dogecoin/', name='Fixing profit')
def test_prices_list(browser):
    browser.get(url)
    assert len(CatalogPage(browser).check_prices_list()) == 12
