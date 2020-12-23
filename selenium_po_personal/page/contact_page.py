from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_po_personal.page.base_page import BasePage


class Contact(BasePage):
    # _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def add_member(self):
        add_name_locator = (By.CSS_SELECTOR, '[name="username"]')
        add_acct_locator = (By.ID, 'memberAdd_acctid')
        add_phone_locator = (By.ID, 'memberAdd_phone')
        save_btn_locator = (By.CSS_SELECTOR, '.js_btn_save')
        self.find_element(add_name_locator).send_keys("Jacky")
        self.find_element(add_acct_locator).send_keys("Jacky1")
        self.find_element(add_phone_locator).send_keys('18926557500')
        self.find_element(save_btn_locator).click()
        return self

    def get_member(self):
        print('x11111111111111111111111111111111111111')
        first_name_locator = (By.CSS_SELECTOR, '.js_ww_table tr:nth-child(1) td:nth-child(2) span')
        WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable(first_name_locator))
        name = self.find_element((By.CSS_SELECTOR, '.js_ww_table tr:nth-child(1) td:nth-child(2) span'))
        print(name.text)
        print('222222222222222222222222222222222222222')
        return name.text

    def get_member2(self):
        first_name_locator = (By.CSS_SELECTOR, '#member_list td:nth-child(2)')
        return self.find_element(first_name_locator).get_attribute("title")
