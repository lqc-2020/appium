from appium.webdriver.common.mobileby import MobileBy
from page.add_member_detail_page import AddMemberDetail

from page.basepage import BasePage


class AddMember(BasePage):
    def goto_add_member_detail(self):
        self.find_and_click(MobileBy.XPATH,"//*[@text='手动输入添加']")
        return AddMemberDetail(self.driver)