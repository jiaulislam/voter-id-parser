from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from typing import Tuple

"""
Module Name: base.py

It is Base class for all page class also
contains the all the generic methods for the 
pages

"""


class BasePage(object):
    def __init__(self, driver: webdriver, timeout: int = 30) -> None:
        self.driver = driver
        self.timeout = timeout

    def find_element(self, *by_locator: Tuple[By, str]):
        """
        Find an element in the DOM Tree
        """
        try:
            return self.driver.find_element(*by_locator)
        except ValueError as e:
            print(e)
        except AttributeError as e:
            print(e)

    def click(self, by_locator: Tuple[By, str]) -> None:
        """
        Click an element on the DOM Tree
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).click()
        except AttributeError as e:
            print(e)

    def write(self, by_locator: Tuple[By, str], text_to_write: str) -> None:
        """
        Write to an element on the DOM Tree
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).send_keys(
                text_to_write)
        except TimeoutException as e:
            print(e)

    def get_element_text(self, by_locator: Tuple[By, str]) -> str:
        """
        Retrieve the 'VALUE' from an element of DOM Tree
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        except TimeoutException as e:
            print(e)
        else:
            return element.text
