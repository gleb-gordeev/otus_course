from page_objects.IndexPage import IndexPage

url = "https://demo.opencart.com/index.php?"


def test_currency(browser):
    browser.get(url)
    IndexPage(browser).change_currency()


def test_header(browser):
    browser.get(url)
    IndexPage(browser).check_header()


def test_products_list(browser):
    browser.get(url)
    assert len(IndexPage(browser).check_products_list()) == 4


def test_cart_add_button(browser):
    browser.get(url)
    IndexPage(browser).check_cart_add_button()


def test_wish_list_button(browser):
    browser.get(url)
    IndexPage(browser).check_wish_list_button()


def test_compare_button(browser):
    browser.get(url)
    IndexPage(browser).check_compare_button()
