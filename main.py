from pages.basepage import BasePage
from selenium import webdriver
from pages.searchresult import SearchResult
import time

URL = "C:\\Users\\Jibon\\Desktop\\JJ\\Verify By Nid.htm"

def parse(driver):
    page = SearchResult(driver)
    nameBangla = page.parse_name_bangla()
    nameEnglish = page.parse_name_english()
    fatherName = page.parse_father_name()
    motherName = page.parse_mother_name()
    return [nameBangla, nameEnglish, fatherName, motherName]
    
if __name__=="__main__":
    driver = webdriver.Firefox(executable_path="C:\\geckodriver-v0.29.1-win64\\geckodriver.exe")
    driver.get(URL)
    names = parse(driver)
    time.sleep(4)
    with open("jst.json", "w", encoding="utf-8") as e:
        for name in names:
            e.write(name+"\n")