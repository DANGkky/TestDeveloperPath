from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def quit(self):
        sleep(5)
        self._driver.quit()
