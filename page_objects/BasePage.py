from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _simple_click_element(self, element):
        element.click()

    def _click(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.browser).move_to_element(element).click().perform()

    def _elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )
