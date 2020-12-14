from test_selenium.page.contact import Contact


class Main:
    def download(self):
        pass

    def import_user(self):
        return self  # 导入用户之后还是返回当前页面进行后续操作，所以可以返回self

    def enter_apps(self):
        pass

    def get_message(self):
        return ['aaa','bbb']

    def add_member(self):
        return Contact()
