from .basepage import BasePage
from selenium.webdriver.common.by import By

class SearchResult(BasePage):
    """
        Child class of BasePage class. This class is exclusivly responsible
        for parsing all the NID holder information.
    """
    # Names, Occupation, Blood-Group, National ID, Pin
    BASIC_INFO = {
        "NAME_BANGLA" : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[2]"),
        "NAME_ENGLISH": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[4]"),
        "FATHER_NAME" : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[8]"),
        "MOTHER_NAME" : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[10]"),
        "SPOUSE_NAME" : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[12]"),
        "DOB"         : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[6]"),
        "OCCUPATION"  : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[14]"),
        "BLOOD_GROUP" : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[20]"),
        "NATIONAL_ID" : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[22]"),
        "PIN"         : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[24]")
    }

    # PRESENT ADDRESS SECTION
    PRESENT_ADDRESS = {
        "PRE_DIVISION"            : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[2]"),
        "PRE_DISTRICT"            : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[4]"),
        "PRE_RMO"                 : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[6]"),
        "PRE_CITY_CORP"           : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[8]"),
        "PRE_UPOZILA"             : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[10]"),
        "PRE_UNION"               : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[12]"),
        "PRE_MOHOLLA"             : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[14]"),
        "PRE_ADDITIONAL_MOHOLLA"  : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[16]"),
        "PRE_WARD_UNION_PARISHAD" : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[18]"),
        "PRE_VILLAGE"             : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[20]"),
        "PRE_ADDITIONAL_ROAD"     : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[22]"),
        "PRE_HOME_HOLDING"        : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[24]"),
        "PRE_POST_OFFICE"         : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[26]"),
        "PRE_POSTAL_CODE"         : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[28]"),
        "PRE_REGION"              : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[30]")
    }

    #PERMENENT ADDRESS
    PERMENENT_ADDRESS = {
        "PERME_DIVISION"            : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[2]"),
        "PERME_DISTRICT"            : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[4]"),
        "PERME_RMO"                 : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[6]"),
        "PERME_CITY_CORP"           : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[8]"),
        "PERME_UPOZILA"             : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[10]"),
        "PERME_UNION"               : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[12]"),
        "PERME_MOHOLLA"             : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[14]"),
        "PERME_ADDITIONAL_MOHOLLA"  : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[16]"),
        "PERME_WARD_UNION_PARISHAD" : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[18]"),
        "PERME_VILLAGE"             : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[20]"),
        "PERME_ADDITIONAL_ROAD"     : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[22]"),
        "PERME_HOME_HOLDING"        : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[24]"),
        "PERME_POST_OFFICE"         : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[26]"),
        "PERME_POSTAL_CODE"         : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[28]"),
        "PERME_REGION"              : (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[30]")
    }

    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def __is_blank(value) -> bool:
        """
        A static method don't depend on the class. Just a simple method to 
        do the string verification
        """
        if value == "":
            return True
        return False

    def _parse_basic_info(self) -> dict:
        """
        Private method
        returns a dictionary with the basic information.
        """
        basic_info = {}
        for key, *selector in self.BASIC_INFO.items():
            parsed_data =self.get_element_text(*selector)
            if self.__is_blank(parsed_data):
                parsed_data = None
            basic_info[key] = parsed_data
        return basic_info

    def _parse_present_address(self) -> list:
        """
        Private method
        returns a list of dictionaries with all the present address information
        """
        present_address_data = {}
        for header, *selector in self.PRESENT_ADDRESS.items():
            parsed_data = self.get_element_text(*selector)
            if self.__is_blank(parsed_data):
                parsed_data = None
            present_address_data[header] = parsed_data

        return present_address_data

    def _parse_permenent_address(self) -> list:
        """
        Private method
        return a list of dictionaries with all the permenent address information
        """
        permenent_address_data = {}
        for header, *selector in self.PERMENENT_ADDRESS.items():
            parsed_data = self.get_element_text(*selector)
            if self.__is_blank(parsed_data):
                parsed_data = None
            permenent_address_data[header] = parsed_data
        return permenent_address_data

    def parse_basic_info(self) -> dict:
        """
        Callable method to get the Basic information of the NID Holder
        """
        return self._parse_basic_info()


    def parse_present_address(self) -> list:
        """
        Callable method to get the present address information of the NID Holder
        """
        return self._parse_present_address()

    def parse_permenent_address(self) -> list:
        """
        Callable method to get the permenent address information of the NID holder
        """
        return self._parse_permenent_address()

