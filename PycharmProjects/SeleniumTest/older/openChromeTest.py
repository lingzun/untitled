#!/usr/bin/python3
#coding:utf-8
import time
import re
from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver=webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.implicitly_wait(8)
driver.get("https://www.baidu.com")
driver.find_element_by_id('kw').send_keys("selenium")
time.sleep(4)
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()

