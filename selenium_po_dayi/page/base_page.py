from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None, _base_url=None):
        if driver is None:
            self._chromeOption = Options()
            # self._chromeOption.add_experimental_option("debuggerAddress", '127.0.0.1:9222')
            # self._driver = webdriver.Chrome(options=self._chromeOption)
            self._driver=webdriver.Chrome()
            self._driver.get("https://work.weixin.qq.com/")
            # self._driver.get(_base_url)
        else:
            self._driver = driver
        self._driver.implicitly_wait(2)
