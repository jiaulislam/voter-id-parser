from typing import Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By

from .basepage import BasePage


class LoginPage(BasePage):
    # Locator Instance Variables
    USERNAME: Tuple[By, str] = (By.ID, "login-username")
    PASSWORD: Tuple[By, str] = (By.ID, "login-password")
    LOGIN_BTN: Tuple[By, str] = (By.ID, "login-button")

    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)

    def insert_username(self, username: str) -> None:
        """
        Insert the username to login to account
        """
        self.find_element(*self.USERNAME).clear()
        self.write(self.USERNAME, username)

    def insert_password(self, password: str) -> None:
        """
        Insert the password to login to account
        """
        self.find_element(*self.PASSWORD).clear()
        self.write(self.PASSWORD, password)

    def click_login_btn(self) -> None:
        """
        Submit the post to request with click action
        """
        self.click(self.LOGIN_BTN)
