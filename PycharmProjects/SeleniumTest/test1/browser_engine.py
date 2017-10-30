#!/usr/bin/python3
#coding:utf-8
from selenium import webdriver
class BrowserEngine(object):
    def __init__(self,driver):
        self.driver=driver
    browser_type="Chrome" #这里可以是Chrome、Firefox、Edge等
    def get_browser(self):
        if self.browser_type=="Ie":
            driver=webdriver.Ie()# 这里IE或Ie都行
        elif self.browser_type=="Firefox":  #注意别写少了字母
            driver=webdriver.Firefox()
        else :
            options=webdriver.ChromeOptions()
            options.add_argument("disable-infobars")
            driver=webdriver.Chrome(chrome_options=options)

        driver.maximize_window()
        driver.implicitly_wait(8)
        return driver

