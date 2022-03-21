from page_objects.ProductPage import ProductPage


def test_product_name(browser):
    browser.open("?route=product/product&product_id=43")
    ProductPage(browser).check_product_name()


def test_price(browser):
    browser.open("?route=product/product&product_id=43")
    ProductPage(browser).check_price()


def test_processor_description(browser):
    browser.open("?route=product/product&product_id=43")
    ProductPage(browser).check_processor_description()


def test_memory_description(browser):
    browser.open("?route=product/product&product_id=43")
    ProductPage(browser).check_memory_description()


def test_case_description(browser):
    browser.open("?route=product/product&product_id=43")
    ProductPage(browser).check_case_description()
