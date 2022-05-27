import datetime
import os
import pytest
import logging
import allure

from selenium import webdriver

DRIVERS = "C:/drivers"


@allure.step('step in conftest.py')
def conftest_step():
    pass


@pytest.fixture
def fixture_conftest_step():
    conftest_step()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.1.105")
    parser.addoption("--url", "-U", default="http://demo.opencart.com")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--bversion")


@pytest.fixture(scope="session", autouse=True)
def get_environment(pytestconfig, request):
    props = {
        'Browser': request.config.getoption("--browser"),
        'Browser.Version': request.config.getoption("--bversion"),
        'Executor': request.config.getoption("--executor"),
        'Stand': 'Production',
        'Shell': os.getenv('SHELL'),
    }

    tests_root = pytestconfig.rootdir
    with open(f'{tests_root}/allure-results/environment.properties', 'w') as f:
        env_props = '\n'.join([f'{k}={v}' for k, v in props.items()])
        f.write(env_props)

    try:
        os.mkdir("logs")
    except Exception as e:
        print(e)


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    log_level = request.config.getoption("--log_level")
    mobile = request.config.getoption("--mobile")
    url = request.config.getoption("--url")
    version = request.config.getoption("--bversion")

    logger = logging.getLogger('driver')
    test_name = request.node.name

    logger.addHandler(logging.FileHandler(f"logs/{test_name}.log"))
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(test_name, datetime.datetime.now()))

    if executor == "local":
        caps = {'goog:chromeOptions': {}}
        if mobile:
            caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}
        driver = webdriver.Chrome(
            executable_path=f"{DRIVERS}/chromedriver", desired_capabilities=caps
        )

    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            "browserVersion": version,
            "name": "Gleb Gordeev",
            "selenoid:options": {"enableVNC": True, "enableVideo": False, "enableLog": True},
            'goog:chromeOptions': {},
        }
        if browser == "chrome" and mobile:
            caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}

        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)
        if not mobile:
            driver.maximize_window()

    def open(path=""):
        return driver.get(url + path)

    driver.test_name = test_name
    driver.log_level = log_level
    driver.open = open
    driver.open()

    logger.info("Browser:{}".format(browser, driver.desired_capabilities))

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(test_name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver
