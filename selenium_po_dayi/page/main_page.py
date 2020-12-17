from selenium.webdriver.common.by import By

from selenium_po_dayi.page.add_member_page import AddMemberPage
from selenium_po_dayi.page.base_page import BasePage


class MainPage(BasePage):
    def add_member(self):
        self._driver.find_element(By.CSS_SELECTOR, '[node-type=addmember]').click()
        return AddMemberPage(self._driver)

    def import_address_book(self):
        pass

    def join_member(self):
        pass