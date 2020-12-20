from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):  # 之前定义driver时，没有说明driver是什么类型。默认是None，所以需要指定是webdriver

        if driver is None:
                self._chromeOption = Options()
                # self._chromeOption.add_experimental_option("debuggerAddress", '127.0.0.1:9222')
                # self._driver = webdriver.Chrome(options=self._chromeOption)
            # else:
                self._driver = webdriver.Chrome()
                self._driver.get(self._base_url)

            # self._driver.get("https://work.weixin.qq.com")
            # self._driver.get("https://work.weixin.qq.com/wework_admin/frame")
            # self._driver.get(self._base_url)
        else:
            self._driver = driver

        self._driver.maximize_window()
        self._driver.implicitly_wait(5)

    def close(self):
        sleep(5)
        self._driver.quit()
