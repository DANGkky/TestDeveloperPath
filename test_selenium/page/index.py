from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.register import Register


class Index(BasePage):
    _base_url = 'https://work.weixi.qq.com/'

    def goto_register(self):
        self.driver.find_element(By.LINK_TEXT, '立即注册').click()  # 点击立即注册
        return Register(self.driver)
