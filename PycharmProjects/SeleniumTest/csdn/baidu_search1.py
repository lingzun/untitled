#!/usr/bin/python3
#coding:utf-8
'''本模块为了演示封装了几个常用selenium方法的base_page.py的使用'''
from time import sleep
from selenium import webdriver
from test1.base_page import BasePage
class Baidu_search1(object):
    options=webdriver.ChromeOptions()#注意这里有个括号
    options.add_argument('disable-infobars')
    driver=webdriver.Chrome(chrome_options=options)

    driver.maximize_window()
    driver.implicitly_wait(5)
    basePage=BasePage(driver)  #使用封装的方法前进行实例化

    def open_baidu(self):
        self.basePage.open_url("https://www.baidu.com") #调用封装的方法使用“self.实例对象.封装方法名”的形式
        sleep(3)

    def test_search(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        sleep(8)
        print(self.driver.title)
        self.basePage.back()
        sleep(3)
        self.basePage.forward()
        sleep(5)
        try:
            assert 'selenium' in self.driver.title
            print("Test pass!")
        except Exception as e:
            print("Test Fail:",format(e))
        self.basePage.quit_browser()
baidu=Baidu_search1()
baidu.open_baidu()
baidu.test_search()