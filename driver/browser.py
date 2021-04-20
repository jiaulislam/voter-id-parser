import static_data as SD
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from actions import OpenURL, DoLogin, GotoNIDVerification


class SingletonBrowser:
    options = Options()
    options.add_argument("--headless")
    __instance = None

    @staticmethod
    def get_browser() -> webdriver:
        if SingletonBrowser.__instance is None:
            SingletonBrowser()
        return SingletonBrowser.__instance

    def __init__(self):
        if SingletonBrowser.__instance is not None:
            pass
        else:
            SingletonBrowser.__instance = webdriver.Firefox(options=self.options,
                                                            executable_path=SD.STATIC_DATA["PATH"])
            OpenURL(SingletonBrowser.__instance, SD.STATIC_DATA["URL"])
            DoLogin(SingletonBrowser.__instance)
            GotoNIDVerification(SingletonBrowser.__instance)
