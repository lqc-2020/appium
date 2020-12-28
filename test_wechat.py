# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWechat:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["noReset"] = "true"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        #caps["ensureWebviewsHavePages"] = True
        caps['settings[waitForIdleTimeout]'] = 0   #设置空闲等待时间为0ms
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()

        
    def test_clock(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("打卡").instance(0));').click()  #滑动查找
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'第')]").click()
        WebDriverWait(self.driver,10).until(lambda x: "外出打卡成功" in x.page_source)
        print(self.driver.page_source)
        assert "外出打卡成功" in self.driver.page_source
