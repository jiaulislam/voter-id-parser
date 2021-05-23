from browser import get_browser_window
from static_data import STATIC_DATA
from actions import (
    OpenURL,
    DoLogin,
    GotoNIDVerification
)

"""
It's a simple module for the first time app
runs then a a remote connection should set
and get the chrome driver the do the one time
task.
"""


def initial_task():
    driver = get_browser_window()  # Connect to remote Chrome
    OpenURL(driver, STATIC_DATA.get('URL'))  # Open the Provided URL
    # DoLogin(driver)  # Login to the website
    # GotoNIDVerification(driver)  # Goto the NID Verification Section


if __name__ == "__main__":
    initial_task()
