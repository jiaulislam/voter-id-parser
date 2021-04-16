from selenium.webdriver.common.by import By

from .basepage import BasePage


class SearchResult(BasePage):
    """
        Child class of BasePage class. This class is exclusivly responsible
        for parsing all the NID holder information.
    """
    # Names, Occupation, Blood-Group, National ID, Pin
    BASIC_INFO = {
        "Name(Bangla)": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[2]"),
        "Name(English)": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[4]"),
        "Father_Name": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[8]"),
        "Mother_Name": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[10]"),
        "Spouse_Name": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[12]"),
        "Date_of_Birth": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[6]"),
        "Occupation": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[14]"),
        "Blood Group": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[20]"),
        "National ID": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[22]"),
        "Pin": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[24]")
    }

    # PRESENT ADDRESS SECTION
    PRESENT_ADDRESS = {
        "Division": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[2]"),
        "District": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[4]"),
        "RMO": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[6]"),
        "City Corporation Or Municipality": (
            By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[8]"),
        "Upozila": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[10]"),
        "Union/Ward": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[12]"),
        "mouza/Moholla": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[14]"),
        "Additional Mouza/Moholla": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[16]"),
        "Ward For Union Porishod": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[18]"),
        "village/Road": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[20]"),
        "Additional Village/Road": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[22]"),
        "Home/Holding No": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[24]"),
        "Post Office": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[26]"),
        "Postal Code": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[28]"),
        "Region": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[16]/div/div[30]")
    }

    # PERMENENT ADDRESS
    PERMENENT_ADDRESS = {
        "Division": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[2]"),
        "District": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[4]"),
        "RMO": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[6]"),
        "City Corporation Or Municipality": (
            By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[8]"),
        "Upozila": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[10]"),
        "Union/Ward": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[12]"),
        "mouza/Moholla": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[14]"),
        "Additional Mouza/Moholla": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[16]"),
        "Ward For Union Porishod": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[18]"),
        "village/Road": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[20]"),
        "Additional Village/Road": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[22]"),
        "Home/Holding No": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[24]"),
        "Post Office": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[26]"),
        "Postal Code": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[28]"),
        "Region": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[18]/div/div[30]")
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
            parsed_data = self.get_element_text(*selector)
            if self.__is_blank(parsed_data):
                parsed_data = None
            basic_info[key] = parsed_data
        return basic_info

    def _parse_present_address(self) -> dict:
        """
        Private method
        returns a dictionaries with all the present address information
        """
        present_address_data = {}
        for header, *selector in self.PRESENT_ADDRESS.items():
            parsed_data = self.get_element_text(*selector)
            if self.__is_blank(parsed_data):
                parsed_data = None
            present_address_data[header] = parsed_data

        return present_address_data

    def _parse_permenent_address(self) -> dict:
        """
        Private method
        return a dictionaries with all the permenent address information
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

    def parse_present_address(self) -> dict:
        """
        Callable method to get the present address information of the NID Holder
        """
        return self._parse_present_address()

    def parse_permenent_address(self) -> dict:
        """
        Callable method to get the permenent address information of the NID holder
        """
        return self._parse_permenent_address()
