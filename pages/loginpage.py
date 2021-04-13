from .basepage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # Locator Instance Variables
    USERNAME = (By.ID, "login-username")
    PASSWORD = (By.ID, "login-password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def insert_username(self, username):
        """
        Insert the username to login to account
        """
        self.find_element(*self.USERNAME).clear()
        self.write(self.USERNAME, username)

    def insert_password(self, password):
        """
        Insert the password to login to account
        """
        self.find_element(*self.PASSWORD).clear()
        self.write(self.PASSWORD, password)

    def click_login_btn(self):
        """
        Submit the post to request with click action
        """
        self.click(self.LOGIN_BTN)