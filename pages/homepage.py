from selenium.webdriver.common.by import By
from .basepage import BasePage


class HomePage(BasePage):
    ID_VERIFICATION_BTN = (By.ID, "DUMMID")

    def __init__(self, driver):
        super().__init__(driver)


    def click_id_verification(self):
        self.click(self.ID_VERIFICATION_BTN)
