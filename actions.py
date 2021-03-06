import sys

from json_formatter.jsonify import export_json
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pages.searchpage import SearchPage
from pages.searchresult import SearchResult
from static_data import STATIC_DATA


def OpenURL(Browser, URL) -> None:
    """
    Open the URL in Browser
    """
    try:
        Browser.get(URL)
    except Exception as e:
        sys.exit(e)


def _check_for_valid_NID(nid_number) -> bool:
    """
    Check if the ID number provided by user is Valid or Not
    """
    if len(nid_number) <= 17 and nid_number.isnumeric():
        return True
    return False


def ExitBrowser(Browser) -> None:
    """
    Exit out of the browser
    """
    try:
        Browser.quit()
    except Exception as e:
        sys.exit(e)


def DoLogin(Browser) -> None:
    """
    Login to the Website
    """
    login_page = LoginPage(Browser)
    login_page.insert_username(STATIC_DATA['USERNAME'])
    login_page.insert_password(STATIC_DATA['PASSWORD'])
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


def DoSearch(Browser, nid_number, dob) -> bool:
    """
    Search action for NID db
    """
    search_page = SearchPage(Browser)
    search_page.insert_NID_number(nid_number)
    search_page.insert_dob(dob)
    search_page.click_search_btn()
    if not search_page.is_search_successful():
        return False
    return True


def ParseSearchResult(Browser) -> dict:
    """
    After Search successful parse the required information
    """
    parser = SearchResult(Browser)
    owner_info = parser.parse_basic_info()
    owner_info.update({'Present Address': parser.parse_present_address()})
    owner_info.update({'Permanent Address': parser.parse_permanent_address()})
    return owner_info


def SearchAction(browser, nid, dob) -> any:
    """
    Search the Shared NID
    """
    browser.refresh()
    flag = DoSearch(browser, nid, dob)
    if flag:
        return export_json(ParseSearchResult(browser))
    else:
        return False
