import logging
#coding = utf-8

from Pages.BasePage import *
from Pages.get_driver import *
import logging


# logging.basicConfig(level=logging.INFO, filename='log3.log',
#                     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
logging.basicConfig(level=logging.INFO, filename='log3.log',
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

class loginPage(BasePage):
    HOME_MENU = ('id','com.gvsoft.gofun:id/iv_menu')
    USER_UNLOGIN = ('id','com.gvsoft.gofun:id/tv_name')
    PHONE_NUM = ('id','com.gvsoft.gofun:id/et_phone')
    LOGIN_NEXT = ('id','com.gvsoft.gofun:id/tv_next_first')
    LOGIN_CAPTCHA = ('id','com.gvsoft.gofun:id/et_sms_code')
    USER_ACCOUNT = ('id','com.gvsoft.gofun:id/tv_name')
    CENTER_TRIP = ('xpath','//*[@text="行程"]')
    trip_datal = ('id','com.gvsoft.gofun:id/tvLabelType')
    back = ('id','com.gvsoft.gofun:id/ib_back')
    CENTER_MONEY = ('xpath', '//*[@text="行程"]')
    dis = ('xpath','//*[@text="分销推广赚钱"]')
    mingxi = ('xpath','//*[@text="查看明细"]')
    tixian = ('id','com.gvsoft.gofun:id/tv_commit_btn')


    def click_dis(self):
        self.click_element(*self.dis)

    def click_homemean(self):
        self.click_element(*self.HOME_MENU)

    def click_headimage(self):
        self.click_element(*self.USER_UNLOGIN)

    def input_phonenumber(self,phonenum):
        self.input_text(phonenum,*self.PHONE_NUM)

    def click_next(self):
        self.click_element(*self.LOGIN_NEXT)

    def input_captcha(self,captcha):
        self.input_text(captcha,*self.LOGIN_CAPTCHA)

    def click_trip(self):
        self.click_element(*self.CENTER_TRIP)

    def click_back(self):
        self.click_element(*self.back)

    def click_money(self):
        self.click_element(*self.CENTER_MONEY)

    def click_mingxi(self):
        self.click_element(*self.mingxi)

    def click_tixian(self):
        self.click_element(*self.tixian)


if __name__ == '__main__':

    driver = get_driver()
    p = loginPage(driver)
    time.sleep(4)
    p.click_homemean()
    time.sleep(4)
    logging.info('click headpic')
    p.click_headimage()
    logging.info('click personal center pic')
    p.input_phonenumber('13091310001')
    logging.info('send phone num')
    p.click_next()
    logging.info('click next')
    p.input_captcha('123456')
    logging.info('send captcha')
    time.sleep(10)
    p.click_homemean()
    p.click_trip()
    time.sleep(4)
    p.click_back()
    # p.click_money()
    # p.click_back()
    time.sleep(6)
    p.click_dis()
    time.sleep(6)
    print(driver.contexts)
    driver.switch_to.context('WEBVIEW_com.gvsoft.gofun')
    time.sleep(6)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/img[2]').click()
    driver.switch_to.context('NATIVE_APP')
    time.sleep(6)
    p.click_mingxi()
    p.press_back()
    p.click_tixian()
    p.press_back()





