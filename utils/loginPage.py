#coding = utf-8
from Pages.BasePage import *
from Pages.get_driver import *
import logging

logging.basicConfig(level=logging.INFO, filename='log1.log',
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
class loginPage(BasePage):
    HOME_MENU = ('id','com.gvsoft.gofun:id/iv_menu')
    USER_UNLOGIN = ('id','com.gvsoft.gofun:id/tv_name')
    PHONE_NUM = ('id','com.gvsoft.gofun:id/et_phone')
    LOGIN_NEXT = ('id','com.gvsoft.gofun:id/tv_next_first')
    LOGIN_CAPTCHA = ('id','com.gvsoft.gofun:id/et_sms_code')

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


if __name__ == '__main__':

    driver = get_driver()
    p = loginPage(driver)
    time.sleep(4)
    p.click_homemean()
    logging.info('点击首页头像')
    p.click_headimage()
    logging.info('点击个人中心头像')
    p.input_phonenumber('13091310001')
    logging.info('输入手机号')
    p.click_next()
    logging.info('点击下一步')
    p.input_captcha('123456')
    logging.info('验证码')
