from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.login import Login
from test_selenium.page.register import Register


class Index(BasePage):
    _base_url = 'https://work.weixi.qq.com/'

    def goto_register(self):
        self._driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()  # 点击立即注册
        return Register(self._driver)

    def goto_login(self):
        self._driver.find_element(By.LINK_TEXT, '企业登录').click()
        return Login(self._driver)