from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://demo.opencart.com/index.php?route=product/category&path=20"


def test_header(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div>h2")))


def test_sort(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[for='input-sort']")))


def test_show(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[for='input-limit']")))


def test_products_list(browser):
    browser.get(url)
    el = browser.find_elements(By.CSS_SELECTOR, "div.product-layout")
    assert len(el) == 5


def test_prices_list(browser):
    browser.get(url)
    el = browser.find_elements(By.CSS_SELECTOR, "div>p.price")
    assert len(el) == 5
