from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                chrome_options = Options()
                chrome_options.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=chrome_options)
            else:
                self._driver = webdriver.Chrome()
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

        self._driver.maximize_window()
        self._driver.implicitly_wait(3)

    def quit(self):
        sleep(5)
        self._driver.quit()

    def find_element(self, by):
        return self._driver.find_element(*by)
