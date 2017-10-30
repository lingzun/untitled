#!/usr/bin/python3
#conding:utf-8
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
options=webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver=webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.implicitly_wait(8)
#点击弹框中的确定
# driver.get("https:www.baidu.com")
# sleep(3)
# driver.execute_script("window.alert('这是一个测试弹框')")
# sleep(2)
# #点击确定
# driver.switch_to.alert().accept()
# #点击取消
# driver.switch_to.alert().dismiss()
#获取页面中全部图片的text，size，tag_name属性
# driver.get("https://news.baidu.com")
# sleep(5)
# for image in driver.find_elements_by_tag_name("img"):
#     print("image.text:",image.text)
#     print("image.size:",image.size)
#     print("image.tag_name:",image.tag_name)
#获取页面中的所有链接(其它属性值也可同样的方法获取到)
# driver.get("https://news.baidu.com")
# sleep(5)
# for href in driver.find_elements_by_xpath("//*[@herf]"):
#     print("链接：",href.get_attribute("herf"))
#3种截图方式
# driver.get("https://www.baidu.com")
# sleep(5)
#一般用这种方法，后面直接加文件路径名称，生成图片文件（图片后缀需为png,否则会报错）
# driver.get_screenshot_as_file("C:\\Users\\wangjf\\Desktop\\one.png")
#生成二进制图片文件，用得少
#driver.get_screenshot_as_png()
#生成base64的编码格式的图片，HTML界面输出截图的时候，会用到
# driver.get_screenshot_as_base64()
driver.quit()
