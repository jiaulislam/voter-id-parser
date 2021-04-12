from .basepage import BasePage
from selenium.webdriver.common.by import By


class Login(BasePage):
    # Locator Instance Variables
    USERNAME = (By.ID, "login-username")
    PASSWORD = (By.ID, "login-password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def insert_username(self, username):
        self.find_element(*self.USERNAME).clear()
        self.write(self.USERNAME, username)

    def insert_password(self, password):
        self.find_element(*self.PASSWORD).clear()
        self.write(self.PASSWORD, password)

    def click_login_btn(self):
        self.click(self.LOGIN_BTN)