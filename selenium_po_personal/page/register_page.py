from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_po_personal.page.base_page import BasePage


class Register(BasePage):
    def register(self, corpname):
        corpname_locator = (By.ID, 'corp_name')
        sub_btn_locator = (By.ID, 'submit_btn')
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(corpname_locator))
        self.find_element(corpname_locator).send_keys(corpname)
        self.find_element(sub_btn_locator).click()
        return self

    def get_error_msg(self):
        error_msg = []
        err_msg_locator = (By.CSS_SELECTOR, '.js_error_msg')
        for msg in self._driver.find_elements(*err_msg_locator):
            error_msg.append(msg.text)
        print(error_msg)
        return error_msg
