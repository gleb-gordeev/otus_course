from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://demo.opencart.com/index.php?route=product/product&product_id=43"


def test_product_name(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1:nth-child(2)")))


def test_price(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.list-unstyled>li>h2")))


def test_processor_description(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p:nth-child(2)")))


def test_memory_description(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p:nth-child(4)")))


def test_case_description(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p:nth-child(6)")))
