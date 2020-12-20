from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_po_dayi.page.base_page import BasePage


class Register(BasePage):
    def register(self, corpname):
        self._driver.find_element(By.ID, 'corp_name').send_keys(corpname)
        WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable((By.ID,'submit_btn')))
        self._driver.find_element(By.ID, 'submit_btn').click()
        return self

    def get_error_msg(self):
        error_msg = []
        for msg in self._driver.find_elements(By.CSS_SELECTOR, '.js_error_msg'):
            error_msg.append(msg.text)
            print(msg.text)
        return error_msg
