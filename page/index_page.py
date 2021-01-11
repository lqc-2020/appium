from appium.webdriver.common.mobileby import MobileBy

from page.address_list_page import AddressList
from page.pre_page import PrePage


class IndexPage(PrePage):
    def goto_address_list(self):
        self.basepage.load("../page/index.yaml")
        #self.basepage.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq' and @text='通讯录']").click()
        return AddressList(self.basepage)
