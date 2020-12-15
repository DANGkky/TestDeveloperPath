from test_selenium.page.index import Index


class TestIndex():

    def setup(self):
        self.index = Index()

    def teardown(self):
        self.index.close()

    def test_register(self):
        # self.driver.find_element(By.PARTIAL_LINK_TEXT, '立即注册').click()  # 点击立即注册
        # self.driver.find_element(By.ID, 'corp_name').send_keys('小游戏测试')
        # self.driver.find_element(By.ID, 'iagree').click()
        # self.driver.find_element(By.ID, 'submit_btn').click()
        self.index.goto_register().register('小游戏测试组')

    def test_login(self):
        register_page = self.index.goto_login().goto_register().register('引擎测试组')
        assert "请选择" in "|".join(register_page.get_error_message())
