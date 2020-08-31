import logging
#coding = utf-8
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from Pages.BasePage import *
from Pages.get_driver import *
import logging


logging.basicConfig(level=logging.INFO, filename='log2.log',
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

class homePage(BasePage):
    HOME_MENU = ('id','com.gvsoft.gofun:id/iv_menu')
    START_SKIP = ('xpath','//*[@text="跳过"]')
    TIME_SHARING = ('xpath','//*[@text="分时"]')
    DAILY_RENT = ('xpath','//*[@text="日租"]')
    WHOLE_RENT = ('xpath','//*[@text="整租"]')
    GO_BUTTON = ('id','com.gvsoft.gofun:id/lottie_go')
    RETURN_SAME_TAKING = ('id','com.gvsoft.gofun:id/tv_same_as_taking')
    HOME_CARD =('id','com.gvsoft.gofun:id/car_bg')
    SELECT_FREE_BTN = ('id','com.gvsoft.gofun:id/img_selectFreeBtn')
    CARD_VIEW = ('id','com.gvsoft.gofun:id/cardView')
    DIALOG_CANCEL = ('id','com.gvsoft.gofun:id/tv_cancel') #确定不购买
    DIALOG_POSITIVE = ('id','com.gvsoft.gofun:id/tv_confirm') #依然购买
    RESERVE_COMMIT = ('id','com.gvsoft.gofun:id/tv_ConfirmPlaceOrder')
    BALANCE_PAYMENT = ('xpath','//*[@text="余额支付"]')
    OPEN_DOOR_CAR = ('xpath', '//*[@text="开门用车"]')
    CAR_RETURN_SETTLEMENT = ('id','com.gvsoft.gofun:id/tv_toReturnCar')
    LOCKING_CAR = ('xpath','//*[@text="锁车并停止计费"]')
    FREE_CAR_RETURN = ('xpath', '免费还车')
    JUST_SO_SO = ('id','com.gvsoft.gofun:id/iv_hai_ke_yi_click')
    BACK_BUTTON = ('id','com.gvsoft.gofun:id/back')
    CAR_RETURN_SETTLEMENT1 = ('id', 'com.gvsoft.gofun:id/tv_return_car')
    RL_ROOT = ('id','com.gvsoft.gofun:id/rl_root')




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

    # 判断日租下单页是否存在日租服务费按钮与点击
    def select_Free_Btn_isExist(self):
        return self.isElementExist(*self.SELECT_FREE_BTN, des="日租服务费按钮")

    def click_select_Free_Btn1(self):
        self.click_element(*self.SELECT_FREE_BTN)

    def click_select_Free_Btn(self):
        try:
            self.find_element(*self.SELECT_FREE_BTN)
        except NoSuchElementException:
            logging.error('元素不存在')
        else:
            self.click_element(*self.SELECT_FREE_BTN)

    def click_cancel(self):
        try:
            self.find_element(*self.DIALOG_CANCEL)
        except NoSuchElementException:
            logging.error('%s 元素不存在')
        else:
            self.click_element(*self.DIALOG_CANCEL)

    def click_open_door_car(self):
        try:
            self.find_element(*self.OPEN_DOOR_CAR)
        except NoSuchElementException:
            logging.error('%s 元素不存在')
        else:
            self.click_element(*self.OPEN_DOOR_CAR)

    def click_car_return_settlement(self):
        try:
            self.find_element(*self.CAR_RETURN_SETTLEMENT)
        except NoSuchElementException:
            logging.error('%s 元素不存在')
        else:
            self.click_element(*self.CAR_RETURN_SETTLEMENT)

    def click_car_return_settlement1(self):
        try:
            self.find_element(*self.CAR_RETURN_SETTLEMENT1)
        except NoSuchElementException:
            logging.error('%s 元素不存在')
        else:
            self.click_element(*self.CAR_RETURN_SETTLEMENT1)

    def click_locking_car(self):
        try:
            self.find_element(*self.LOCKING_CAR)
        except NoSuchElementException:
            logging.error('%s 元素不存在')
        else:
            self.click_element(*self.LOCKING_CAR)

    def click_back_button(self):
        try:
            self.find_element(*self.BACK_BUTTON)
        except NoSuchElementException:
            logging.error('%s 元素不存在')
        else:
            self.click_element(*self.BACK_BUTTON)



    # 判断日租下单页是否存在日租服务费按钮与点击
    def card_view_isExist(self):
        return self.isElementExist(*self.CARD_VIEW, des="弹窗")

    def click_dialog_cancel(self):
        self.click_element(*self.DIALOG_CANCEL)

    def click_dialog_positive(self):
        self.click_element(*self.DIALOG_POSITIVE)

    # 判断下单页确认签署并下单是否存在与点击
    def ConfirmPlaceOrder_isExist(self):
        return self.isElementExist(*self.RESERVE_COMMIT, des="确认签署并下单")

    def click_ConfirmPlaceOrder(self):
        if self.ConfirmPlaceOrder_isExist():
            self.click_element(*self.RESERVE_COMMIT)

    # 判断下单页确认签署并下单是否存在与点击
    def just_so_so_isExist(self):
        return self.isElementExist(*self.JUST_SO_SO, des="还可以")

    def click_just_so_so(self):
        if self.just_so_so_isExist():
            self.click_element(*self.JUST_SO_SO)

    # 判断下单页确认签署并下单是否存在与点击
    def balance_payment_isExist(self):
        return self.isElementExist(*self.BALANCE_PAYMENT, des="余额支付")

    def click_balance_payment(self):
        if self.balance_payment_isExist():
            self.click_element(*self.BALANCE_PAYMENT)

    def click_rl_root(self):
        try:
            self.find_element(*self.RL_ROOT)
        except NoSuchElementException:
            pass
        else:
            self.click_element(*self.RL_ROOT)

    def daily_rent_order(self):
        logging.info('======================日租下单开始=======================')
        logging.info("点击首页日租tab")
        self.click_element(*self.DAILY_RENT)
        time.sleep(4)
        # logging.info("点击GO按钮")
        # self.click_element(*self.GO_BUTTON)
        # time.sleep(4)
        logging.info("点击同取车点按钮")
        self.click_element(*self.RETURN_SAME_TAKING)
        time.sleep(4)
        logging.info("点击车辆卡片")
        self.click_element(*self.HOME_CARD)
        time.sleep(4)
        logging.info("点击日租服务费选择框")
        self.click_select_Free_Btn()
        time.sleep(4)
        logging.info("确认取消日租服务费")
        self.click_dialog_cancel()
        time.sleep(4)
        logging.info("确认下单")
        self.click_ConfirmPlaceOrder()
        time.sleep(4)
        logging.info("点击确认下单弹窗")
        self.click_dialog_positive()
        time.sleep(4)
        logging.info("余额支付")
        self.click_balance_payment()
        time.sleep(4)
        logging.info("点击开门用车")
        self.click_open_door_car()
        time.sleep(4)
        logging.info("点击确认开门用车")
        self.click_dialog_positive()
        time.sleep(4)
        logging.info("点击还可以")
        self.click_just_so_so()
        time.sleep(4)
        logging.info("点击还车结算")
        self.click_car_return_settlement()
        time.sleep(4)
        logging.info("点击锁车并停止计费")
        self.click_locking_car()
        time.sleep(4)
        logging.info("点击返回按钮")
        self.click_back_button()
        logging.info('======================日租下单结束=======================')

    def time_sharing_order(self):
        logging.info('======================分时下单开始=======================')
        logging.info("点击首页分时tab")
        self.click_element(*self.TIME_SHARING)
        time.sleep(4)
        # logging.info("点击GO按钮")
        # self.click_element(*self.GO_BUTTON)
        # time.sleep(4)
        logging.info("点击同取车点按钮")
        self.click_element(*self.RETURN_SAME_TAKING)
        time.sleep(4)
        logging.info("点击车辆卡片")
        self.click_element(*self.HOME_CARD)
        time.sleep(4)

        logging.info("点击确认签署并下单按钮")
        self.click_ConfirmPlaceOrder()
        time.sleep(4)
        logging.info("点击确认预定")
        self.click_dialog_positive()
        time.sleep(4)
        logging.info("点击开门用车")
        self.click_open_door_car()
        time.sleep(4)
        logging.info("点击确认开门用车")
        self.click_dialog_positive()
        time.sleep(4)
        logging.info("点击还可以")
        self.click_just_so_so()
        time.sleep(4)
        logging.info("点击去还车按钮")
        self.click_car_return_settlement1()
        time.sleep(4)
        logging.info("点击锁车并停止计费")
        self.click_locking_car()
        time.sleep(4)

        logging.info("余额支付")
        self.click_balance_payment()
        time.sleep(4)

        logging.info("点击页面关闭分享")
        self.click_rl_root()
        time.sleep(4)

        logging.info("点击返回按钮")
        self.click_back_button()
        logging.info('======================分时下单结束=======================')




if __name__ == '__main__':

    driver = get_driver()
    hp = homePage(driver)

    if hp.start_skip_isExist():
        hp.click_start_skip()

    driver.find_element_by_id('com.gvsoft.gofun:id/iv_location_icon').click()
    time.sleep(4)

    for i in range(2):
        hp.zoom()
        hp.get_screen_shot()

    for i in range(2):
        hp.pinch()
        hp.get_screen_shot()
    # hp = homePage(driver)
    #
    # if hp.start_skip_isExist():
    #     hp.click_start_skip()
    #
    # time.sleep(5)
    # hp.daily_rent_order()
    # time.sleep(5)
    # hp.time_sharing_order()

