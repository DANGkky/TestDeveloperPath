from selenium.webdriver.common.by import By

from selenium_po_personal.page.base_page import BasePage
from selenium_po_personal.page.register_page import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self._driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)
