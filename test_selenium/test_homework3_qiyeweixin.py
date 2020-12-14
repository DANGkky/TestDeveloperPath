from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestQiYeWeiXin():
    def setup(self):
        # chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"  cmd直接敲入命令即可启动单独的调试chrome
        # chromeOptions = Options()
        # chromeOptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # self.driver = webdriver.Chrome(options=chromeOptions)
        chromeOptions = Options()
        chromeOptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # chromeOptions.add_argument("debuggerAddress","127.0.0.1:9222")  这个命令可以不？
        self.driver = webdriver.Chrome(options=chromeOptions)
        # chrome --remote-debugging-port=9222
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    def test_contacts(self):
        self.driver.find_element(By.ID, "menu_contacts").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ww_operationBar div:nth-child(1) .js_add_member").click()
        self.driver.find_element(By.ID, 'username').send_keys('Jacky')
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys('Jacky_test')
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys('18926577777')
        self.driver.find_element(By.CSS_SELECTOR, 'qui_btn ww_btn js_btn_save').click()
