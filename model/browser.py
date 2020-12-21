# -*- coding: utf-8 -*-
# @Time : 2020/12/19 17:00
# @Author : nichao
# @Email : 530504026@qq.com
# @File : browser.py
# @Project : appAuto
from appium import webdriver
def open_app():
    desired_capabilities = {'platformName': 'Android',
                            'deviceName': '127.0.0.1:5554',
                            'platformVersion': '7.1.2',
                            'appPackage': 'com.meishio.app',
                            'appActivity': 'module.home.activity.SplashActivity',
                            'unicodeKeyboard': True,
                            'newCommandTimeout': 100,
                            'noRest': True,
                            'resetKeyboard': True
                            }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    driver.implicitly_wait(30)
    return driver