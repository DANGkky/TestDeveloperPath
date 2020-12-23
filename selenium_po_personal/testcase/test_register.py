from selenium_po_personal.page.index import Index


class TestRegister:

    def setup(self):
        self.index = Index(reuse=False)

    def teardown(self):
        # self.index.quit()
        pass

    def test_register(self):
        register_page = self.index.goto_register().register('小游戏测试组')
        assert "请选择" in '|'.join(register_page.get_error_msg())
