from selenium.webdriver.common.by import By

from selenium_po_personal.page.base_page import BasePage
from selenium_po_personal.page.contact_page import Contact


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contact(self):
        add_member_locator = (By.CSS_SELECTOR, '[node-type="addmember"]')
        self.find_element(add_member_locator).click()
        return Contact(reuse=True)
