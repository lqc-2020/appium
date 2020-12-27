from appium.webdriver.common.mobileby import MobileBy

from page.address_list_page import AddressList
from page.basepage import BasePage


class IndexPage(BasePage):
    def goto_address_list(self):
        self.find(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/elq' and @text='通讯录']").click()
        return AddressList(self.driver)
