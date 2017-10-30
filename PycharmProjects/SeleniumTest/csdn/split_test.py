#!/usr/bin/env python3
#coding:utf-8
from selenium import webdriver
from time import sleep
class Split_test(object):
    def __init__(self):
       pass

    def get_search_result(self):
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        driver = webdriver.Chrome(chrome_options=options)
        driver.maximize_window()
        driver.implicitly_wait(8)
        driver.get("https://www.baidu.com")
        sleep(5)
        driver.find_element_by_id("kw").send_keys("selenium")
        sleep(5)
        driver.find_element_by_id('kw').clear()
        sleep(3)
        original_str=driver.find_element_by_xpath("//*[@class='nums']").text
        print(original_str)
        new_str=original_str.split('约')[1]#1表示切割（留下）“约”后面的部分内容
        print(new_str)
        last_str=new_str.split('个')[0]#0表示切割（留下）“个”前面的部分内容
        print(last_str)
        driver.quit()
one=Split_test()
one.get_search_result()

