import logging
from time import sleep

import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from page.black_handle import black_wrapper


class BasePage:
    FIND = 'find'
    ACTION = 'action'
    FIND_AND_CLICK = 'find_and_click'
    SEND = 'find_and_send'
    CONTENT = 'content'
    SLIDE = 'slide'
    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["noReset"] = "true"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["automationName"] = 'Uiautomator2'
        # caps["ensureWebviewsHavePages"] = True
        # caps['settings[waitForIdleTimeout]'] = 0  # 设置空闲等待时间为0ms
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
        self.black_list = [(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/idp']")]

    @black_wrapper
    def find(self,By,locator):
        return self.driver.find_element(By,locator)

    def finds(self,By, locator):
        return self.driver.find_elements(By, locator)

    def find_and_click(self,By,locator):
        return self.find(By,locator).click()


    def slide(self,name):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                         .scrollable(true).instance(0))\
                                         .scrollIntoView(new UiSelector()\
                                         .text("{name}").instance(0));')

    def find_and_send(self,by,locator,text):
        return self.find(by,locator).send_keys(text)

    def time_wait(self):
        return WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))

    def load(self,yaml_path):
        with open(yaml_path,'r',encoding='utf-8') as f:
            data = yaml.load(f)
        for ele in data:
            xpath_expr = ele.get(self.FIND)
            action = ele.get(self.ACTION)
            if action == self.FIND_AND_CLICK:
                self.find_and_click(MobileBy.XPATH,xpath_expr)
            elif action == self.SEND:
                content = ele.get(self.CONTENT)
                self.find_and_send(MobileBy.XPATH,xpath_expr,content)
            elif action == self.SLIDE:
                self.slide(xpath_expr).click()


    def res(self):
        try:
            WebDriverWait(self.driver,10,0.1).until(self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
            result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
            return result
            # WebDriverWait(self.driver, 10,0.05).until(lambda x: x.find_element(MobileBy.XPATH, "//*[contains(@text,'添加成功')@class='android.widget.Toast']"))
            # result = self.find(MobileBy.XPATH, "//*[@class='androexcept:
        except:
            print('没找到toast')

    def screenshot(self, picture_path):
        self.driver.save_screenshot(picture_path)