from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def navigate(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        try:
            self.wait_for_element(*locator)
            element = self.driver.find_element(*locator)
            return element
        except (NoSuchElementException, TimeoutException) as error:
            print(error)
            return None

    def wait_for_element(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, *locator):
        element = self.find_element(*locator)
        if element is not None:
            element.click()
        else:
            print('cannot find element')

    def click_element_not_interactable(self, *locator):
        element = self.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_element_text(self, *locator):
        element = self.find_element(*locator)
        if element is not None:
            text = element.text
            if not text:
                if element.get_attribute('innerText'):
                    text = element.get_attribute('innerText')
                elif element.get_attribute('innerHTML'):
                    text = element.get_attribute('innerHTML')
            return text
        return None

    def input_keys(self, keys, *locator):
        txt = self.find_element(*locator)
        txt.send_keys(keys)
