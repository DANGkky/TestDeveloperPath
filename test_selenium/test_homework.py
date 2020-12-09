from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestSeleniumWork():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com")
        self.driver.implicitly_wait(5)  # ！！！隐式等待  可以解决元素已经加载出来，但是因为dom同步等各种问题而不可点击的问题，会在设定时间内不断刷新尝试点击

    def teardown(self):
        pass

    def test_open_hogwarts(self):
        '''
        耶可以了
        '''
        self.driver.set_window_size(2000, 1000)
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        element = (By.CSS_SELECTOR, "[data-name=\"求职面试圈\"]")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        # self.driver.find_element_by_css_selector("#main-nav-menu > ul > li:nth-child(4) > a").click()
        # sleep(2)  # ！！！固定等待  可以解决元素还没有加载出来就尝试寻找并点击的问题，不太推荐
        self.driver.find_element(*element).click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".topic:nth-child(1) .title a").click()
