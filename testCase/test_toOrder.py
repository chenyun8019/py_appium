#coding=utf-8
from appium import webdriver
from Pages.get_driver import *
import time


ad_pic = driver.find_element_by_id('com.gvsoft.gofun:id/ad_img')
ad_close = driver.find_element_by_id('com.gvsoft.gofun:id/iv_close')
if ad_pic.is_displayed():
    ad_close.click()
else:
    print('无广告图')
driver.find_element_by_xpath('//*[@text="日租"]').click()
time.sleep(5)
ad_pic1 = driver.find_element_by_id('com.gvsoft.gofun:id/ad_img')
ad_close1 = driver.find_element_by_id('com.gvsoft.gofun:id/iv_close')
if ad_pic1.is_displayed():
    ad_close1.click()
else:
    print('无广告图')

driver.find_element_by_id('com.gvsoft.gofun:id/tv_city').click()
driver.find_element_by_id('com.gvsoft.gofun:id/location_city_name').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@text="日租"]').click()
time.sleep(5)
driver.find_element_by_id('com.gvsoft.gofun:id/lottie_go').click()
driver.find_element_by_id('com.gvsoft.gofun:id/tv_same_as_taking').click()
driver.find_element_by_id('com.gvsoft.gofun:id/lin_plate').click()

fwf_btn = driver.find_element_by_id('com.gvsoft.gofun:id/img_selectFreeBtn')

if fwf_btn.is_displayed():
    fwf_btn.click()

diolog = driver.find_element_by_id('com.gvsoft.gofun:id/cardView')
cancel = driver.find_element_by_id('com.gvsoft.gofun:id/tv_cancel')
if diolog.is_displayed():
    cancel.click()

driver.find_element_by_id('com.gvsoft.gofun:id/tv_ConfirmPlaceOrder').click()
time.sleep(3)
title = driver.find_element_by_id('com.gvsoft.gofun:id/tv_Title')
print(title.text)

driver.find_element_by_id('com.gvsoft.gofun:id/tv_pay_name').click()
driver.find_element_by_xpath('//*[@text="开门用车"]').click()
diolog = driver.find_element_by_id('com.gvsoft.gofun:id/cardView')
confirm = driver.find_element_by_id('com.gvsoft.gofun:id/tv_confirm')
if diolog.is_displayed():
    confirm.click()
time.sleep(4)
driver.find_element_by_id('com.gvsoft.gofun:id/iv_hai_ke_yi_click').click()
# far_dio = driver.find_element_by_id('com.gvsoft.gofun:id/car_sofar_rl')
# far_close = driver.find_element_by_id('com.gvsoft.gofun:id/car_sofar_close')
# if far_dio.is_displayed():
#     far_close.click()
time.sleep(5)
driver.find_element_by_xpath('//*[@text="还车结算"]').click()
time.sleep(2)
driver.find_element_by_id('com.gvsoft.gofun:id/tv_commit_btn').click()
driver.find_element_by_id('com.gvsoft.gofun:id/back').click()