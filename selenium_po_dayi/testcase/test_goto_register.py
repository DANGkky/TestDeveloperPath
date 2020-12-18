from time import sleep

from selenium_po_dayi.page.index import Index


class TestGotoRegister():

    def setup(self):
        self.index = Index()

    def teardown(self):
        sleep(5)
        self.index.quit()

    def test_goto_register(self):
        register_page = self.index.goto_register().register('小游戏测试组')
        result = register_page.get_error_msg()
        assert '请选择' in '|'.join(result)
