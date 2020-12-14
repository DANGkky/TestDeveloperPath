from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
        self.driver.maximize_window()
        '''
        尝试直接新开一个页面打开企业微信，失败！！！还是需要扫码，必须要复用
        self.driver.get("https://work.weixin.qq.com/")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".index_top_operation_loginBtn")))
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        sleep(5)
        '''
        # chrome --remote-debugging-port=9222
        self.driver.implicitly_wait(2)

    def teardown(self):
        sleep(5)
        # self.driver.quit()

    def test_contacts(self):
        self.driver.find_element(By.ID, "menu_contacts").click()
        WebDriverWait(self.driver, 10).until(self.wait_element)  # 记得这里的wait_element不能带括号！！！
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ww_operationBar:nth-child(1) .js_add_member')))
        # self.driver.find_element(By.CSS_SELECTOR, '.ww_operationBar:nth-child(1) .js_add_member').click()
        self.driver.find_element(By.ID, 'username').send_keys('Jacky')
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys('Jacky_test')
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys('18926577777')
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()

    def wait_element(self, x):
        size = len(self.driver.find_elements(By.ID, 'username'))
        if size < 1:
            # self.driver.find_element(By.CSS_SELECTOR, '.ww_operationBar:nth-child(1) .js_add_member').click()
            self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        return size >= 1  #这个return的内容  不能放在if循环里
