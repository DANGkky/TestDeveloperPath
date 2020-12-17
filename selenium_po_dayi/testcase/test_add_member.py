from selenium_po_dayi.page.main_page import MainPage


class TestAddMember:
    def test_add_member(self):
        mainPage = MainPage()
        mainPage.add_member().add_member2()


