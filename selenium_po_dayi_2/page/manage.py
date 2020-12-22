from selenium.webdriver.common.by import By

from selenium_po_dayi_2.page.base_page import BasePage


class Manage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#manageTools"

    def load_picture(self):
        material_locator = (By.CSS_SELECTOR, '[href="#material/text"]')
        goto_picture_locator = (By.CSS_SELECTOR, '[href="#material/image"]')
        goto_upload_locator = (By.CSS_SELECTOR, '.js_upload_file_selector')
        upload_locator = (By.CSS_SELECTOR, '#js_upload_input')
        self.find_element(material_locator).click()
        self.find_element(goto_picture_locator).click()
        self.find_element(goto_upload_locator).click()
        self.find_element(upload_locator).send_keys('D:/Users/Desktop/Test_material.png')

    def get_picture(self):
        first_picture_locator = (By.CSS_SELECTOR, '.material_picCard_cnt_pic')
        return self.find_element(first_picture_locator).get_attribute("style")
