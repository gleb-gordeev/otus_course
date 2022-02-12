from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://demo.opencart.com/index.php?route=account/register"


def test_header(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content>h1")))


def test_help_text(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content>p")))
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div#content>p"),
            "If you already have an account with us, please login at the login page.",
        )
    )
    assert el.text == "If you already have an account with us, please login at the login page."


def test_first_name(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='firstname']")))


def test_last_name(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='lastname']")))


def test_email(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='email']")))
