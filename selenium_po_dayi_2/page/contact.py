from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_po_dayi_2.page.base_page import BasePage


class Contact(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def add_member(self):
        id_locator = (By.CSS_SELECTOR, '[name="username"]')
        acct_id_locator = (By.ID, 'memberAdd_acctid')
        gender_female_locator = (By.CSS_SELECTOR, '.ww_radio[value="2"]')
        zip_code_locator = (By.CSS_SELECTOR, '.ww_telInput_zipCode')
        macao_locator = (By.CSS_SELECTOR, '[data-value="853"]')
        tell_number_locator = (By.ID, 'memberAdd_phone')
        save_locator = (By.CSS_SELECTOR, '.js_btn_save')
        # WebDriverWait(self._driver, 5).until(expected_conditions.element_to_be_clickable(id_locator))
        # self.find_element(id_locator).send_keys("Jacky")
        # self.find_element(acct_id_locator).send_keys("Jacky")
        # self.find_element(gender_female_locator).click()
        # self.find_element(zip_code_locator).click()
        # self.find_element(macao_locator).click()
        # self.find_element(tell_number_locator).send_keys("18926577566")
        WebDriverWait(self._driver, 5).until(expected_conditions.element_to_be_clickable(save_locator))
        self.find_element(save_locator).click()
        # return self

    def get_member(self):
        # 考虑添加显示等待
        first_member_locator = (By.CSS_SELECTOR, '#member_list td:nth-child(2)')
        return self.find_element(first_member_locator).get_attribute("title")
