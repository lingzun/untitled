#!/usr/bin/python3
#conding:utf-8
class BasePage(object):
    """主要把selenium中几个常用的方法封装到BasePage类中，这里演示了几个方法"""
    """back(),forward(),get(),quit()"""
    def __init__(self,driver):
        """构造函数，有一个参数，driver"""
        self.driver=driver

    def back(self):
        #后退操作
        self.driver.back()

    def forward(self):
        #前进操作
        self.driver.forward()

    def open_url(self,url):
        #进入某个url网址
        self.driver.get(url)

    def quit_browser(self):
        #退出浏览器
        self.driver.quit()