from selenium.webdriver.common.by import By
from selenium_po_dayi_2.page.base_page import BasePage
from selenium_po_dayi_2.page.contact import Contact


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        goto_addmember_locator = (By.CSS_SELECTOR, '[node-type="addmember"]')
        self.find_element(goto_addmember_locator).click()
        return Contact(reuse=True)
