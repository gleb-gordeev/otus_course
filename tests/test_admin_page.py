from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

url = "https://demo.opencart.com/admin/"


def test_check_header_logo(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#header-logo>a>img")),
        message='Logo not found',
    )


def test_check_help_text(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.panel-title")))
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "h1.panel-title"), "Please enter your login details."
        )
    )
    assert el.text == "Please enter your login details."


@pytest.mark.parametrize("field", ['[name="username"]', '[name="password"]'])
def test_check_fields(browser, field):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, field)))
    el.click()


def test_check_forgot_password(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.help-block")))
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "span.help-block"), "Forgotten Password"
        )
    )
    el.click()
    assert el.text == "Forgotten Password"


def test_check_login_button(browser):
    browser.get(url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.help-block")))
    el.click()
