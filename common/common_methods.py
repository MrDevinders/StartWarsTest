from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

waitForElementTime = 10

class CommonMethods:

    def __init__(self, driver) -> None:
        self.driver = driver

    def webelement_input(self, locator, text):
        WebDriverWait(self.driver, waitForElementTime).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def webelement_click(self, locator):
        WebDriverWait(self.driver, waitForElementTime).until(EC.visibility_of_element_located(locator)).click()

    def webelement_exist(self, locator):
        return WebDriverWait(self.driver, waitForElementTime).until(EC.visibility_of_element_located(locator)).is_displayed()
