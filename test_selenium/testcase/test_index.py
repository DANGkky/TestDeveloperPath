from test_selenium.page.index import Index


class TestIndex():

    def setup(self):
        self.index = Index()

    def test_register(self):
        # self.driver.find_element(By.PARTIAL_LINK_TEXT, '立即注册').click()  # 点击立即注册
        # self.driver.find_element(By.ID, 'corp_name').send_keys('小游戏测试')
        # self.driver.find_element(By.ID, 'iagree').click()
        # self.driver.find_element(By.ID, 'submit_btn').click()
        self.index.goto_register().register('小游戏测试组')
