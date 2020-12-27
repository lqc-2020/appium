from appium import webdriver

from page.basepage import BasePage
from page.index_page import IndexPage


class App(BasePage):
    def start(self):
        caps = {}
        caps["platformName"] = "android"
        caps["noReset"] = "true"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # caps["ensureWebviewsHavePages"] = True
        caps['settings[waitForIdleTimeout]'] = 0  # 设置空闲等待时间为0ms
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)
        return self

    def goto_index_page(self):
        # 进入到首页
        return IndexPage(self.driver)
