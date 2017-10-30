#!/usr/bin/python3
#coding:utf-8
from time import sleep
from selenium import webdriver
class Baidu_search(object):
    options=webdriver.ChromeOptions()#注意这里有个括号
    options.add_argument('disable-infobars')
    driver=webdriver.Chrome(chrome_options=options)

    driver.maximize_window()
    driver.implicitly_wait(5)

    def open_baidu(self):
        self.driver.get("https://www.baidu.com")
        sleep(3)

    def test_search(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        sleep(8)
        print(self.driver.title)
        try:
            assert 'selenium' in self.driver.title
            print("Test pass!")
        except Exception as e:
            print("Test Fail:",format(e))
        self.driver.quit()
baidu=Baidu_search()
baidu.open_baidu()
baidu.test_search()