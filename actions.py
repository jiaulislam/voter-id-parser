from selenium import webdriver
from pages.loginpage  import LoginPage
from pages.homepage import HomePage
from pages.searchpage import SearchPage
from pages.searchresult import SearchResult
import static_data as sd
import sys

def OpenBrowser() -> webdriver:
    """
    Return a webdriver object with FireFox browser
    """
    return webdriver.Firefox(executable_path=sd.STATIC_DATA["PATH"])

def OpenURL(Browser, URL) -> None:
    """
    Open the URL in Browser
    """
    Browser.get(URL)

def _check_for_valid_NID(nid_number) -> bool:
    """
    Check if the ID numbe provided by user is Valid or Not
    """
    if len(nid_number) < 17 and nid_number.isnumeric():
        return True
    return False

def ExitBrowser(Browser) -> None:
    """
    Exit out of the browser
    """
    Browser.quit()

def DoLogin(Browser) -> None:
    """
    Login to the Website
    """
    login_page = LoginPage(Browser)
    login_page.insert_username(sd.STATIC_DATA['USERNAME'])
    login_page.insert_password(sd.STATIC_DATA['PASSWORD'])
    login_page.click_login_btn()

def GotoNIDVerification(Browser) -> None:
    """
    Click on the NID Verification Menu Button
    """
    home_page = HomePage(Browser)
    home_page.click_id_verification()


def take_arguments() -> tuple:
    """
    Take input from User
    """
    nid_number = input("Enter NID number: ")
    if _check_for_valid_NID(nid_number):
        dob = input("Enter DOB(Required Format: YYYY-MM-DD): ")
    else:
        sys.exit("Invalid NID number !")
    return nid_number, dob

def DoSearch(Browser, nid_number, dob) -> None:
    """
    Search aciton for NID db
    """
    search_page = SearchPage(Browser)
    search_page.insert_NID_number(nid_number)
    search_page.insert_dob(dob)
    search_page.click_search_btn()
    # exit out of program if search not successfull
    if not search_page.is_search_successful():
        sys.exit("NID Information Not Found !")

def Parse_Search_Result(Browser) -> dict:
    """
    After Search successful parse the required information
    """
    parser = SearchResult(Browser)
    result = parser.parse_basic_info()
    present_address = parser.parse_present_address()
    permenent_address = parser.parse_permenent_address()
    result['Present Address'] = present_address
    result['Permanent Address'] = permenent_address
    return result
