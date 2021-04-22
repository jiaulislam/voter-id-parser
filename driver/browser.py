from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

"""
This module will initiate a bridge to work
with existing instance of a Chrome Browser.
"""

BROWSER = "9999"  # set this to desired 4 digit port


def __remote_handler(port: str) -> Options:
    options = Options()
    options.add_experimental_option("debuggerAddress", f"localhost:{port}")
    return options


def get_browser_window() -> webdriver:
    return webdriver.Chrome(ChromeDriverManager().install(), options=__remote_handler(BROWSER))
