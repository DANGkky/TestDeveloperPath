from selenium.webdriver.common.by import By

from selenium_po_dayi.page.base_page import BasePage


class Register(BasePage):
    def register(self, corpname):
        self._driver.find_element(By.ID, 'corp_name').send_keys(corpname)
        self._driver.find_element(By.ID, 'submit_btn').click()
        return self

    def get_error_msg(self):
        error_msg = []
        for msg in self._driver.find_elements(By.CSS_SELECTOR, '.js_error_msg'):
            error_msg.append(msg.text)
            print(msg.text)
        return error_msg
