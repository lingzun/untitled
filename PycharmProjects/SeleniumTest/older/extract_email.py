#!usr/bin/python3
import re
# from time import sleep
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://www.baidu.com")
#使用try except进行测试断言
try:
    #使用id查找element的方法
    # driver.find_element_by_tag_name("form")
    #使用link text查找element的方法
    # driver.find_element_by_link_text("新闻")
    #也可以这样写
    # driver.find_element_by_xpath("//div[@id='u_sp']/a[text()='新闻']")
    # driver.find_element_by_xpath("//*/a[herf='http://news.baidu.com']")          #未完成，待学习后重新获取
    #使用partical link text查找element的方法（相当于link text的contain，只需输入链接文字的部分字符，）
    # driver.find_element_by_partial_link_text("主页")
    #通过class name查找element的方法
    # driver.find_element_by_class_name("s_tab")
    #通过name属性查找element的方法
    # driver.find_element_by_name("wd")
    #通过css selector查找element的方法：
    # driver.find_element_by_css_selector("#su")
    #get输入框中输入selenium
    #driver.find_element_by_id("kw").send_keys("selenium")
    #清空输入框
    #driver.find_element_by_id("kw").clear()
    #获取输入框的值
    #text=driver.find_element_by_id("kw").get_attribute("value")
    # 网页刷新
    # driver.refresh()
    #执行后退
    # driver.back()
    #执行前进
    # driver.forward()
    #获取浏览器版本号  capabilities是容器的意思
    # version=driver.capabilities["version"]
    #获取当前网页的网址
    # url=driver.current_url
    #获取当前网页的标题
    # title=driver.title
    sleep(3)
    #键位操作，需要导入Keys模块：from selenium.webdriver.common.keys import Keys
    # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL,'n')
    #ele = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'n')   有问题的方式
    # driver.find_element_by_link_text("登录").click()
    # sleep(5)
    #遍历点击新闻界面的2个单选控件
    # radios=driver.find_elements_by_xpath("//*/input[@type='radio']")
    # for radio in radios:
    #     radio.click()
    #     time.sleep(5)
    #点击复选框（2种方法）
    # checker=driver.find_elements_by_xpath("//*/input[@type='checkbox']")
    # checker=driver.find_elements_by_xpath("//*[@name='memberPass']")
    # for check in checker:
    #     check.click()
    #获取当前浏览器窗口的大小
    # original_size=driver.get_window_size()
    # print("当前窗口大小为：",original_size)
    #设置浏览器窗口的大小（宽度，高度）
    # driver.set_window_size(720,480)
    # driver.set_window_size(original_size["width"],original_size["height"])
    print("test pass:test found,")
except Exception as e:
    print("Exception found",format(e))
driver.quit()