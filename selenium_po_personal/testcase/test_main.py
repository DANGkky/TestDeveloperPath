from selenium_po_personal.page.main_page import Main


class TestMain:

    def setup(self):
        self.main = Main(reuse=True)

    def teardown(self):
        self.main.quit()

    def test_add_member(self):
        self.contact = self.main.goto_contact().add_member()
        assert self.contact.get_member() == 'Jacky'

    def test_import_user(self):
        self.main.import_user('xxx.file')
        assert 'success' in self.main.get_msg()

    def test_send_msg(self):
        pass
