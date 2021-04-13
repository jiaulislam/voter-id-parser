from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .basepage import BasePage

class SearchPage(BasePage):
    """
    With the help of this class user should able to enter the NID & DOB in the DOM Tree
    """
    NID_TEXT = (By.ID, "nidVoterInput")
    DOB_TEXT = (By.ID, "dateOfBirth")
    SEARCH_BTN = (By.ID, "btnVerify")
    # below one edge case need to handle if the ID num or DOB is wrong then 
    RESULT = (By.ID, "//*[@id='result-container']/div[2]/div/div/div")
    EDGE_CASE = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[30]")

    def __init__(self, driver):
        super().__init__(driver)

    def insert_NID_number(self, nid_number) -> None:
        """
        Insert the NID number for query
        """
        self.find_element(*self.NID_TEXT).clear()
        self.write(self.NID_TEXT, nid_number)

    def insert_dob(self, date_of_birth) -> None:
        """
        Insert the Date of birth for query.

        Note: As the DOB element is not able to take text from selenium, executing javascript 
        Fixing the data at the DOM level
        """
        code = f"document.getElementById('dateOfBirth').setAttribute('value', '{date_of_birth}');"
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(self.DOB_TEXT))
        except TimeoutException:
            return
        else:
            self.driver.execute_script(code)

    def click_search_btn(self) -> None:
        """
        Click on the search button after the DOB & NID has been given
        """
        self.click(self.SEARCH_BTN)

    def is_search_successful(self) -> bool:
        """
        A edge case need to handle when a NID is not found in that case return False else True
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(self.EDGE_CASE))
        except TimeoutException:
            return False
        else:
            return True
