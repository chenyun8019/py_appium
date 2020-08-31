#coding=utf-8

from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
import os
import time

class BasePage:
    timeOut = 5000
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

    #获取手机屏幕尺寸
    def get_screen_size(self):
        screen_size = self.driver.get_window_size()
        return screen_size
        # x = screen_size['width']
        # y = screen_size['height']

    # 缩小屏幕
    def pinch(self):
        action1 = TouchAction(self.driver)
        action2 = TouchAction(self.driver)
        action3 = MultiAction(self.driver)
        x = self.get_screen_size()['width']
        y = self.get_screen_size()['height']
        action1.press(x=0.3 * x, y=0.3 * y).wait(200).move_to(x=0.4 * x, y=0.4 * y).wait(200).release()
        action2.press(x=0.8 * x, y=0.8 * y).wait(200).move_to(x=0.7 * x, y=0.7 * y).wait(200).release()
        action3.add(action1, action2)
        print('开始缩小')
        action3.perform()

    # 放大屏幕
    def zoom(self):
        action1 = TouchAction(self.driver)
        action2 = TouchAction(self.driver)
        action3 = MultiAction(self.driver)
        x = self.get_screen_size()['width']
        y = self.get_screen_size()['height']
        action1.press(x=0.4 * x, y=0.4 * y).wait(200).move_to(x=0.3 * x, y=0.3 * y).wait(200).release()
        action2.press(x=0.7 * x, y=0.7 * y).wait(200).move_to(x=0.8 * x, y=0.8 * y).wait(200).release()
        action3.add(action1, action2)
        print('开始放大')
        action3.perform()


    def get_screen_shot(self):

        path = os.path.dirname(os.path.abspath('.')) + '\screenShot\\'
        print(path)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        print(current_time)
        file_name = path + current_time + '.png'
        self.driver.get_screenshot_as_file(file_name)

    def swipe_up(self):
        x = self.get_screen_size()['width']
        y = self.get_screen_size()['height']
        self.driver.swipe(x*0.5,y*0.7,x*0.5, y*0.5,self.timeOut)

    def swipe_up(self,timeOut):
        x = self.get_screen_size()['width']
        y = self.get_screen_size()['height']
        self.driver.swipe(x*0.5,y*0.7,x*0.5, y*0.5,timeOut)










