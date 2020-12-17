from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):  # 之前定义driver时，没有说明driver是什么类型。默认是None，所以需要指定是webdriver
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)
            self._driver.get("https://work.weixin.qq.com")

            # self.driver.get(self._base_url)
        else:
            self._driver = driver

    def close(self):
        sleep(10)
        self._driver.quit()
