from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://demo.opencart.com/index.php?"


def test_header(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1>a")))


def test_products_list(browser):
    browser.get(url)
    el = browser.find_elements(By.CSS_SELECTOR, "div.product-layout")
    assert len(el) == 4


def test_cart_add_button(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    el = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.button-group>button:nth-child(1)"))
    )
    el.click()


def test_wish_list_button(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    el = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.button-group>button:nth-child(2)"))
    )
    el.click()


def test_compare_button(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    el = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.button-group>button:nth-child(3)"))
    )
    el.click()
