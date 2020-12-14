from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_retry():
    def setup(self):
        option = Options()
        option.add_experimental_option('debuggingAddress', '127.0.0.1')
        self.driver = webdriver.Chrome(options=option)
        self.driver.get('https://work.weixin.qq.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_real(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(By.CSS_SELECTOR,'.active'))
        self.driver.find_element(By.CSS_SELECTOR,'.active').click()



