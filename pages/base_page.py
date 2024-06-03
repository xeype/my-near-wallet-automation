from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://testnet.mynearwallet.com/'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_element_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Element is not clickable by locator {locator}")

    def is_element_clickable(self, locator, time=10):
        try:
            WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Element is not clickable by locator {locator}")
            return True
        except TimeoutException:
            return False

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def is_element_visible(self, locator, time=10):
        try:
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Element is not visible by locator {locator}")
            return True
        except TimeoutException:
            return False

    def open_website(self, url=None):
        if url is not None:
            return self.driver.get(self.base_url)
