from appium.webdriver.common.mobileby import MobileBy
from page.add_member_detail_page import AddMemberDetail

from page.basepage import BasePage
from page.pre_page import PrePage


class AddMember(PrePage):
    def goto_add_member_detail(self):
        self.basepage.load("../page/add_member.yaml")
        #self.basepage.find_and_click(MobileBy.XPATH,"//*[@text='手动输入添加']")
        return AddMemberDetail(self.basepage)