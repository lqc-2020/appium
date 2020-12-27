import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    def find(self,By,locator):
        return self.driver.find_element(By,locator)

    def find_and_click(self,By,locator):
        return self.find(By,locator).click()


    def slide(self,text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                         .scrollable(true).instance(0))\
                                         .scrollIntoView(new UiSelector()\
                                         .text("{text}").instance(0));')

    def find_and_send(self,by,locator,text):
        return self.find(by,locator).send_keys(text)

    def time_wait(self):
        return WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))


    def res(self):
        return self.driver.page_source