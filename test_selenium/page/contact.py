from selenium.webdriver.common.by import By


class Contact():
    # _add_member_button = (By.CSS, 'XXX')  # 类的方法，等于是页面page的内部方法，不需要暴露给外部。所以在名称前添加下划线。外部就无法引用

    def add_member(self, data):
        # self.driver.find_element("添加成员").click()
        # sendkeys
        # click_save
        return self

    def add_member_error(self, data):
        return member_ListPage()  # 对于相同的PO，不同的测试数据返回不同的页面时，需要创建不同的页面方法。

    def search(self):
        pass

    def import_users(self, data):
        pass

    def export_user(self):
        pass

    def set_department(self, data):
        pass

    def delete(self):
        pass

    def invite(self):
        pass

    def add_department(self):
        pass


