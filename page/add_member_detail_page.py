from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage


class AddMemberDetail(BasePage):
    def save(self,name,phone,sex):
        self.find_and_send(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../*[@text='必填']",name)
        self.find_and_click(MobileBy.XPATH,"//*[contains(@text, '性别')]/..//*[@text='男']")
        if sex == '男':
            self.time_wait()
            self.find_and_click(MobileBy.XPATH,"//*[@text='男']")
        elif sex == '女':
            self.find_and_click(MobileBy.XPATH,"//*[@text='女']")
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']",phone)
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        return self