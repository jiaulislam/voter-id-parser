from selenium.webdriver.common.by import By

from .basepage import BasePage


class SearchResult(BasePage):
    """
        Child class of BasePage class. This class is exclusively responsible
        for parsing all the NID holder information.
    """
    # Names, Occupation, Blood-Group, National ID, Pin
    BASIC_INFO = {
        "Name(Bangla)": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[2]"),
        "Name(English)": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[4]"),
        "Father Name": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[8]"),
        "Mother Name": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[10]"),
        "Spouse Name": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[12]"),
        "Date of Birth": (By.XPATH, "//*[@id='result-container']/div[3]/div[1]/div/div[6]"),
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

    # PERMANENT ADDRESS
    PERMANENT_ADDRESS = {
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

    def __parser(self, data: dict) -> dict:
        """
        Return a parsed dictionary modeled data
        :param data: dict
        :return: dict: formatted data of NID Holder information
        """
        information = {}
        for key, *selector in data.items():
            parsed_data = self.get_element_text(*selector)
            if self.__is_blank(parsed_data):
                parsed_data = None
            information.update({key: parsed_data})
        return information

    def parse_basic_info(self) -> dict:
        """
        Callable method to get the Basic information of the NID Holder
        """
        return self.__parser(self.BASIC_INFO)

    def parse_present_address(self) -> dict:
        """
        Callable method to get the present address information of the NID Holder
        """
        return self.__parser(self.PRESENT_ADDRESS)

    def parse_permanent_address(self) -> dict:
        """
        Callable method to get the permanent address information of the NID holder
        """
        return self.__parser(self.PERMANENT_ADDRESS)
