import logging
#coding = utf-8

from Pages.BasePage import *
from Pages.get_driver import *
import logging


logging.basicConfig(level=logging.INFO, filename='log3.log',
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

class homePage(BasePage):
    HOME_MENU = ('id','com.gvsoft.gofun:id/iv_menu')
    START_SKIP = ('xpath','//*[@text="跳过"]')

    #判断首页头像是否存在与点击
    def home_menu_isExist(self):
        return self.isElementExist(*self.HOME_MENU,des="首页头像")

    def click_home_menu(self):
        self.click_element(*self.HOME_MENU)

    #判断启动页跳过按钮是否存在与点击
    def start_skip_isExist(self):
        return self.isElementExist(*self.START_SKIP,des="启动页跳过")

    def click_start_skip(self):
        self.click_element(*self.START_SKIP)




if __name__ == '__main__':

    driver = get_driver()
    hp = homePage(driver)

    if hp.start_skip_isExist():
        hp.click_start_skip()

    time.sleep(5)
    if hp.home_menu_isExist():
        print(hp.home_menu_isExist())
        hp.click_home_menu()
