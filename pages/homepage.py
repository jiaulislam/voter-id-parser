from typing import Tuple

from selenium.webdriver.common.by import By
from selenium import webdriver

from .basepage import BasePage


class HomePage(BasePage):
    ID_VERIFICATION_BTN: Tuple[By, str] = (By.ID, "verificationImg")

    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)

    def click_id_verification(self) -> None:
        """
        Click on the ID Verification Menu button on DOM Tree
        """
        self.click(self.ID_VERIFICATION_BTN)
