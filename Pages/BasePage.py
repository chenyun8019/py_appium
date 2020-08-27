#coding=utf-8
from appium import webdriver
import time
import logging
class BasePage:
    def __init__(self,driver):
        self.driver = driver
    #封装查找元素方法（通过find_element）
    def find_element(self,*locator):
        self.driver.find_element(*locator)

    # 封装查找元素方法（通过find_elements）
    def find_elements(self,*locator):
        self.driver.find_elements(*locator)

    def switch_to_webview(self):
        web_view = 'WEBVIEW_com.gvsoft.gofun'
        contexts_list = self.driver.contexts()
        for context in contexts_list:
            if context.text :
                self.driver.switch_to.context()

    # 封装手机返回键
    def press_back(self):
        self.driver.keyevent(4)

    # 封装点击元素方法
    def click_element(self,*locator):
        self.driver.find_element(*locator).click()

    # 封装输入文本方法
    def input_text(self,text,*locator):
        self.driver.find_element(*locator).send_keys(text)

    # 封装元素是否存在方法
    def isElementExist(self,*locator,des=None):
        element = self.driver.find_elements(*locator)
        if len(element) == 0:
            print("元素未找到:%s" %des)
            return False
        elif len(element) == 1:
            return True
        else:
            print("找到%s个元素:%s" % (len(element), locator))
            return False

    a =3








