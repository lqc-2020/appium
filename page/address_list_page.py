from appium.webdriver.common.mobileby import MobileBy

from page.add_member import AddMember
from page.basepage import BasePage
from page.pre_page import PrePage


class AddressList(PrePage):
    def goto_add_member(self):
        self.basepage.load("../page/address_list.yaml")
        #self.basepage.slide("添加成员").click()
        return AddMember(self.basepage)