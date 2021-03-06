from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):  # 之前定义driver时，没有说明driver是什么类型。默认是None，所以需要指定是webdriver
        if driver is None:
            self._driver = webdriver.Chrome()

        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

        self._driver.maximize_window()
        self._driver.implicitly_wait(5)

    def close(self):
        sleep(5)
        self._driver.quit()
