from idlelib import window
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_Homework2():
    def setup(self):
        # options=webdriver.ChromeOptions()
        # options.add_argument(options.headless)
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com")

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_homework(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(By.PARTIAL_LINK_TEXT,"中国软件测试行业问卷调研"))
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"中国软件测试行业问卷调研").click()
        self.driver.switch_to.window(self.driver.window_handles[1])