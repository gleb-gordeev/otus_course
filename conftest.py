import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DRIVERS = "C:/drivers"


def choose_browser(browser):
    if browser == "chrome":
        service = Service(executable_path=os.path.join(DRIVERS, "chromedriver"))
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = Service(executable_path=os.path.join(DRIVERS, "geckodriver"))
        driver = webdriver.Firefox(service=service)
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    else:
        raise Exception("Driver not supported")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://demo.opencart.com/")


@pytest.fixture
def browser(request):
    driver = choose_browser(request.config.getoption("--browser"))
    request.addfinalizer(driver.quit)
    return driver
