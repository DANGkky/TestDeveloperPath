from selenium_po_personal.page.main import Main


class TestRegister:

    def setup(self):
        self.main = Main()

    def teardown(self):
        self.main.quit()

    def test_register(self):
        register_page = self.main.goto_register().register('小游戏测试组')
        assert "请选择" in '|'.join(register_page.get_error_msg())
