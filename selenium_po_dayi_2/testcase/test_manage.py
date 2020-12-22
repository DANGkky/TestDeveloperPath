from selenium_po_dayi_2.page.manage import Manage


class TestManage():

    def setup(self):
        self.manage = Manage(reuse=True)

    def test_manage(self):
        self.manage.load_picture()
        assert "Test_material.png" in self.manage.get_picture()

        # ActionChains(self._driver).move_to_element(self.find_element(xxx)).perform()
