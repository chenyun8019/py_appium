#coding=utf-8
from appium import webdriver
import time
def get_driver():
    desired_caps={
        "automationName":"UiAutomator2",
        "platformName":"Android",
        "platformVersion":'9',
        "deviceName":"5ENDU19123014140",#adb devices查看
        "appPackage":"com.gvsoft.gofun",#获取命令：aapt dump badging apk路径，查看package
        "appActivity":"com.gvsoft.gofun.module.splash.activity.SplashActivity",#获取命令：aapt dump badging apk路径，查看launchable-activity
        "noReset":True#在此会话之前，请勿重置应用程序状态
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    driver.implicitly_wait(6)

    return driver


if __name__ == '__main__':
    get_driver()

