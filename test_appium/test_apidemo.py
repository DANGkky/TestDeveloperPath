from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "Jacky"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["automationName"] = "uiautomator2"
        # caps["unicodeKeyboard"] = True  # 键盘可以输入中文
        # caps["resetKeyboard"] = True  # 测试完成后充值键盘为输入英文
        caps["autoGrantPermissions"] = True
        caps["noReset"] = True
        caps["dontStopAppOnReset"] = True
        caps["skipServerInstallation"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # sleep(20)
        # self.driver.quit()
        pass

    def test_toast(self):
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new Uiselector().text("views").instance(0));')
        self.driver.find_element(*scroll_to_element).click()

        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_to_element).click()

        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'Make a Popup!').click() #对于空间有content_des字段的，用ACCESSIBILITY_ID

        self.driver.find_element(By.XPATH, "//*[@text='Search']").click()
        toast = self.driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text
        print(toast)
        assert "Search" in toast
        assert "Clicked" in toast


    def test_uiselector(self):
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("Views").instance(0));')
        self.driver.find_element(*scroll_to_element).click()
        # print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)

    def test_scroll(self):
        size = self.driver.get_window_size()
        for i in range(10):
            TouchAction(self.driver).long_press(x=size['width'] * 0.5, y=size['height'] * 0.8) \
                .move_to(x=size['width'] * 0.5, y=size['height'] * 0.2).release().perform()

    def test_source(self):
        print(self.driver.page_source)

    def test_device(self):
        self.driver.background_app(5)
        self.driver.lock(5)
        self.driver.unlock()
