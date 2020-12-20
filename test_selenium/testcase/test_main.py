from test_selenium.page.main import Main


class TestMain():
    def test_add_member(self):
        main = Main(reuse=True)
        main.add_member().add_member('xxx')
        assert 'aaa' in main.import_user().get_message()

    def test_import_user(self):
        main.import_user("xxx.file")
        assert "success" in main.get_message()

    def test_send_msg(self):
        main.send_message()
        assert  "" in main.get_message()
