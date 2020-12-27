from appium.webdriver.common.mobileby import MobileBy

from page.add_member import AddMember
from page.basepage import BasePage


class AddressList(BasePage):
    def goto_add_member(self):
        self.slide("添加成员").click()
        #self.find_and_click(MobileBy.XPATH,"//*[@text='添加成员']")
        return AddMember(self.driver)