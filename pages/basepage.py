from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

"""
Module Name: base.py

It is Base class for all page class also
contains the all the generic methods for the 
pages

"""

class BasePage(object):
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout
    
    def find_element(self, *by_locator):
        try:
            return self.driver.find_element(*by_locator)
        except ValueError as e:
            print(e)
        except AttributeError as e:
            print(e)

    def click(self, by_locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).click()
        except AttributeError as e:
            print(e)

    def write(self, by_locator, text_to_write):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).send_keys(text_to_write)
        except TimeoutException as e:
            print(e)

    def get_element_text(self, by_locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).get_attribute("value")
        except TimeoutException as e:
            print(e)
        else:
            return element