from selenium import webdriver
URL = "https://prportal.nidw.gov.bd/partner-portal/login/"

def run_browser():
    driver = webdriver.Firefox(executable_path="C:\\geckodriver\\geckodriver.exe")
    driver.get(URL)
    
if __name__=="__main__":
    run_browser()