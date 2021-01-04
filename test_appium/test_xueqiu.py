from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "Jacky"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["automationName"] = "uiautomator2"
        caps["unicodeKeyboard"] = True  # 键盘可以输入中文
        caps["resetKeyboard"] = True  # 测试完成后充值键盘为输入英文
        caps["autoGrantPermissions"] = True
        caps["noReset"] = False
        caps["dontStopAppOnReset"] = True
        caps["skipServerInstallation"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # sleep(20)
        # self.driver.quit()
        pass

    def test_search(self):
        # WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located()) #显示等待
        self.driver.find_element(MobileBy.ID, "tv_agree").click()  # 清数据后重启时，要点击同意使用协议。
        self.driver.find_element(MobileBy.ID, "home_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys('alibaba')
        self.driver.find_element(MobileBy.ID, "search_input_text").click()
        self.driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="阿里巴巴-SW"]').click()
        self.driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="股票"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="09988"]/../../..//*[contains(@resource-id,"follow_btn")]').click()
        a = self.driver.find_element(MobileBy.XPATH,
                                     '//*[@text="09988"]/../../..//*[contains(@resource-id,"current_price")]').text
        assert float(a) > 200
        print(self.driver.find_element(MobileBy.XPATH,
                                       '//*[@text="09988"]/../../..//*[contains(@resource-id,"current_price")]').get_attribute(
            'resourceId'))


    def test_scroll(self):
        size = self.driver.get_window_size()
        for i in range(10):
            TouchAction(self.driver).long_press(x=size['width'] * 0.5, y=size['height'] * 0.8) \
                .move_to(x=size['width'] * 0.5, y=size['height'] * 0.2).release().perform()

    def test_xpath(self):
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@text="09988"]/../../..//*[contains(@resource-id,"current_price")]')

    def test_source(self):
        print(self.driver.page_source)

    def test_device(self):
        self.driver.background_app(5)
        self.driver.lock(5)
        self.driver.unlock()
