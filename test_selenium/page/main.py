from test_selenium.page.base_page import BasePage
from test_selenium.page.contact import Contact


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def download(self):
        pass

    def import_user(self):
        return self  # 导入用户之后还是返回当前页面进行后续操作，所以可以返回self

    def enter_apps(self):
        pass

    def get_message(self):
        return ['aaa', 'bbb']

    def add_member(self):
        return Contact()
