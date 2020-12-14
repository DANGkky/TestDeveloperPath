from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

'''
课后作业问题总结：
1、自定义until的method时，需要确保有返回值（return不能是false）。
2、在cmd里直接启动单独的chrome时，需要确保其他chrome窗口关闭，并且chrome.exe在环境变量中有配置
3、关注自定义方法  wait_element  的定义时的参数数量，因为until的函数中有method，具体实现中是要传入_self.driver参数，所以要在wait_element里添加一个接收这个参数的参数位置
'''


class TestQiYeWeiXin():
    def setup(self):
        # chrome --remote-debugging-port=9222  cmd直接敲入命令即可启动单独的调试chrome，需要其他chrome窗口关闭，并且chrome.exe放在环境变量里

        chromeOptions = Options()
        chromeOptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=chromeOptions)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def teardown(self):
        sleep(5)
        # self.driver.quit()

    def test_contacts(self):
        self.driver.find_element(By.ID, "menu_contacts").click()
        WebDriverWait(self.driver, 10).until(self.wait_element)  # 记得这里的wait_element不能带括号！！！
            # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
            # '.ww_operationBar:nth-child(1) .js_add_member'))) self.driver.find_element(By.CSS_SELECTOR,
            # '.ww_operationBar:nth-child(1) .js_add_member').click()
        self.driver.find_element(By.ID, 'username').send_keys('Jacky')
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys('Jacky_test')
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys('18926577777')
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()

    def wait_element(self, x):
        size = len(self.driver.find_elements(By.ID, 'username'))
        if size < 1:
            self.driver.find_element(By.CSS_SELECTOR, '.ww_operationBar:nth-child(1) .js_add_member').click()
        return size >= 1  #这个return的内容  不能放在if循环里
