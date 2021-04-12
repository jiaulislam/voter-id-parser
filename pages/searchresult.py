from .basepage import BasePage
from selenium.webdriver.common.by import By

class SearchResult(BasePage):
    # Names, Occupation, Blood-Group, National ID, Pin
    NAME_BANGLA = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[2]")
    NAME_ENGLISH= (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[4]")
    FATHER_NAME = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[8]")
    MOTHER_NAME = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[10]")
    SPOUSE_NAME = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[12]")
    DOB         = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[6]")
    OCCUPATION  = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[14]")
    BLOOD_GROUP = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[20]")
    NATIONAL_ID = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[22]")
    PIN         = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[24]")

    # PRESENT ADDRESS SECTION
    PRE_DIVISION            = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[2]")
    PRE_DISTRICT            = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[4]")
    PRE_RMO                 = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[6]")
    PRE_CITY_CORP           = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[8]")
    PRE_UPOZILA             = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[10]")
    PRE_UNION               = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[12]")
    PRE_MOHOLLA             = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[14]")
    PRE_ADDITIONAL_MOHOLLA  = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[16]")
    PRE_WARD_UNION_PARISHAD = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[18]")
    PRE_VILLAGE             = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[20]")
    PRE_ADDITIONAL_ROAD     = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[22]")
    PRE_HOME_HOLDING        = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[24]")
    PRE_POST_OFFICE         = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[26]")
    PRE_POSTAL_CODE         = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[28]")
    PRE_REGION              = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[30]")

    #PERMENENT ADDRESS
    PERME_DIVISION            = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[2]")
    PERME_DISTRICT            = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[4]")
    PERME_RMO                 = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[6]")
    PERME_CITY_CORP           = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[8]")
    PERME_UPOZILA             = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[10]")
    PERME_UNION               = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[12]")
    PERME_MOHOLLA             = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[14]")
    PERME_ADDITIONAL_MOHOLLA  = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[16]")
    PERME_WARD_UNION_PARISHAD = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[18]")
    PERME_VILLAGE             = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[20]")
    PERME_ADDITIONAL_ROAD     = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[22]")
    PERME_HOME_HOLDING        = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[24]")
    PERME_POST_OFFICE         = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[26]")
    PERME_POSTAL_CODE         = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[28]")
    PERME_REGION              = (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[30]")

    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def __is_blank(value):
        if value == "":
            return True
        return False

    def _parse_name_bangla(self):
        val = self.get_element_text(self.NAME_BANGLA)
        if self.__is_blank(val):
            return None
        return val

    def _parse_name_english(self):
        val = self.get_element_text(self.NAME_ENGLISH)
        if self.__is_blank(val):
            return None
        return val

    def _parse_father_name(self):
        val = self.get_element_text(self.FATHER_NAME)
        if self.__is_blank(val):
            return None
        return val

    def _parse_mother_name(self):
        val = self.get_element_text(self.MOTHER_NAME)
        if self.__is_blank(val):
            return None
        return val

    def parse_basic_info(self):
        pass

    def parse_present_address(self):
        pass

    def parse_permenent_address(self):
        pass
