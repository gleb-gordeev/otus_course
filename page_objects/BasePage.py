import logging

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser, wait=3):
        self.browser = browser
        self.wait = WebDriverWait(browser, wait)
        self.actions = ActionChains(browser)
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.addHandler(logging.FileHandler(f"logs/{self.browser.test_name}.log"))
        self.logger.setLevel(level=self.browser.log_level)

    def open(self, url):
        self.logger.info("Opening url: {}".format(url))
        self.browser.get(url)

    def click(self, locator):
        self.logger.info("Clicking element: {}".format(locator))
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_and_submit(self, locator, value):
        self.logger.info("Input {} in input {}".format(value, locator))
        find_field = self.wait.until(EC.presence_of_element_located(locator))
        find_field.click()
        find_field.clear()
        find_field.send_keys(value)

    def is_present(self, locator):
        try:
            self.logger.info("Check if element {} is present".format(locator))
            return self.wait.until(EC.visibility_of_element_located(locator))
        except NoSuchElementException or TimeoutException:
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG,
            )
            raise AssertionError(f"Element {locator} not found on page!")

    def _elements(self, locator):
        self.logger.info("Check if elements {} is present".format(locator))
        return self.wait.until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )
