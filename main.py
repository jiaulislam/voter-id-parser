from selenium import webdriver
from pages.searchresult import SearchResult
from pages.loginpage  import Login
from pages.homepage import HomePage
from pages.searchpage import SearchPage
import json

URL = "C:\\Users\\Jibon\\Desktop\\JJ\\Verify By Nid.htm"

def nid_parser(driver):
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

    # search_page = SearchPage(driver)
    # search_page.insert_dob("1995-03-10")







    ########## EXPORT #############
    all_information = nid_parser(driver)
    # To export JSON file
    with open("parsed_data.json", "w") as json_file:
        writer = json.dumps(all_information, indent=4)
        json_file.writelines(writer)

    # To Read JSON file
    with open('parsed_data.json', "r") as read_json:
        data = json.loads(read_json.read())
        for i,v in data.items():
            print(i, "->", v)

    driver.quit()
