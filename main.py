from os import name
from pages.basepage import BasePage
from selenium import webdriver
from pages.searchresult import SearchResult
import time
import json

URL = "C:\\Users\\Jibon\\Desktop\\JJ\\Verify By Nid.htm"

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
    for i , v in parse(driver).items():
        print(i , "-> ", v)