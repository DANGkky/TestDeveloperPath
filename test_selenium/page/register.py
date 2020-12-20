from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.page.base_page import BasePage


class Register(BasePage):

    def register(self, corpname):
        # WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'corp_name')))
        self._driver.find_element(By.ID, 'corp_name').send_keys(corpname)
        # self._driver.find_element(By.ID, 'iagree').click()
        # WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'submit_btn')))
        self._driver.find_element(By.ID, 'submit_btn').click()
        return self

    def get_error_message(self):
        error_message = []
        for element in self._driver.find_elements(By.CSS_SELECTOR, '.js_error_msg'):
            error_message.append(element.text)
            print(element.text)
        return error_message
