from appium.webdriver.common.mobileby import MobileBy


from page.pre_page import PrePage


class AddMemberDetail(PrePage):
    def save(self,name,phone,sex):
        self.basepage.find_and_send(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../*[@text='必填']",name)
        self.basepage.find_and_click(MobileBy.XPATH,"//*[contains(@text, '性别')]/..//*[@text='男']")
        if sex == '男':
            self.basepage.time_wait()
            self.basepage.find_and_click(MobileBy.XPATH,"//*[@text='男']")
        elif sex == '女':
            self.basepage.find_and_click(MobileBy.XPATH,"//*[@text='女']")
        self.basepage.find_and_send(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']",phone)
        self.basepage.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        self.basepage.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.wework:id/idp")').click()
        try:
            res = self.basepage.slide(name)
            return res.text

        except:
            print('没有找到元素')

