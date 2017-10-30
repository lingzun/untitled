#!/usr/bin/env python3
#coding:utf-8
from time import sleep
from selenium import webdriver
from test1.logger import Logger
mylogger=Logger(logger='TestMyLog').getLog()#从loger.py模块中获取已经定义好的mylogger对象。
class TestMyLog(object):
    def print_log(self):
        options=webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        driver=webdriver.Chrome(chrome_options=options)
        driver.maximize_window()
        driver.implicitly_wait(8)
        mylogger.info("打开浏览器")
        driver.get("https://www.baidu.com")
        mylogger.info("打开百度首页")#打印INFO级别的log
        mylogger.debug("打开百度首页1")#打印DEBUG级别的log
        mylogger.error("打开百度首页2")#打印error级别的log
        sleep(5)
        mylogger.info("暂停5秒")
        driver.quit()
        mylogger.info("关闭并退出浏览器")
testlog=TestMyLog()
testlog.print_log()


