from selenium import webdriver
from pages.searchresult import SearchResult
from pages.loginpage  import Login
from pages.homepage import HomePage
from pages.searchpage import SearchPage
import json

URL = "C:\\Users\\Jibon\\Downloads\\unsuccessfull\\Verify By Nid.htm"

def parse(driver=None):
    page = SearchResult(driver)
    basic_info = page.parse_basic_info()
    present_address = page.parse_present_address()
    permenent_address = page.parse_permenent_address()
    basic_info['present_address'] = present_address
    basic_info['permenent_address'] = permenent_address
    return basic_info
    
    
if __name__=="__main__":
    driver = webdriver.Firefox(executable_path="C:\\geckodriver-v0.29.1-win64\\geckodriver.exe")
    driver.get(URL)

    search_page = SearchPage(driver)
    search_page.insert_dob("1995-03-10")







    ########## EXPORT #############
    # all_information = parse(driver)
    # # To export JSON file
    # with open("parsed_data.json", "w") as json_file:
    #     writer = json.dumps(all_information, indent=4)
    #     json_file.writelines(writer)

    # driver.quit()
