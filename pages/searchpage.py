from selenium.webdriver.common.by import By
from .basepage import BasePage

class SearchPage(BasePage):
    NID_TEXT = (By.ID, "nidVoterInput")
    DOB_TEXT = (By.ID, "dateOfBirth")
    SEARCH_BTN = (By.ID, "btnVerify")
    RESULT = (By.ID, "RESULT")

    def __init__(self, driver):
        super().__init__(driver)

    def insert_NID_number(self, nid_number):
        self.find_element(*self.NID_TEXT).clear()
        self.write(self.NID_TEXT, nid_number)

    def insert_dob(self, date_of_birth):
        self.find_element(*self.DOB_TEXT)
        self.write(self.DOB_TEXT, date_of_birth)

    def click_search_btn(self):
        self.click(self.SEARCH_BTN)

    def is_search_successful(self):
        pass