#!usr/bin/python3
#coding:utf-8
# import sys
# sys.setdefaultencoding("utf-8")
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
options=webdriver.ChromeOptions()
options.add_argument("disable-infobars")
driver=webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.implicitly_wait(8)
try:
    # driver.get("http://news.baidu.com/")
    # sleep(3)
    # #第一种断言方法(通过断言函数)
    # assert "百度一下" in driver.title
    # print("Assertion test pass")
    # sleep(1)
    # #第二种断言方法（通过if判断是否相等）
    # if "百度一下，你就知道"==driver.title:
    #     print("Assertion test1 pass")
    #点击登录
    #driver.find_element_by_xpath("//*[@id='u1']/a[@name='tj_login']").click()
    #点击登录（未输入登录账号的情况下）
    #driver.find_element_by_xpath("//*/input[@id='TANGRAM__PSP_10__submit']").click()
    #断言方法一（通过判断包含目标属性的对象是否出现的方式），获取属性的值用text（）  有括号的
    #driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__error' and text()='请您输入手机/邮箱/用户名']").is_displayed()
    #断言方法二（推荐方法），通过对象的属性获取到对象的其它属性，断言该属性是否等于要查找对象的值
    #获取对象的的值用.text  没有括号
    # str=driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__error']").text
    # assert str=="请您输入手机/邮箱/用户名"
    #判断单选或者多选控件是否被选中，或者下拉选择菜单是否选择一个默认的option，is_selected()返回的是一个boolean变量
    # one=driver.find_element_by_xpath("//*/input[@id='news']").is_selected()
    # if one:
    #     print("Test pass")
    #获取网页元素的大小
    # ele=driver.find_element_by_xpath("//*[@id='sugarea']/span[2]/input") 或者
    # ele=driver.find_element_by_xpath("//*[@id='sugarea']/span/input[@value='百度一下']")
    # print("‘百度一下’ 的大小为：",ele.size)
    #执行全选（Control + a）
    # ele=driver.find_element_by_tag_name("body")
    # ele.send_keys(Keys.CONTROL+'a')
    #删除输入框中的文本
    # driver.find_element_by_id("ww").send_keys("selenium runoob")
    # driver.find_element_by_id("ww").send_keys(Keys.BACKSPACE)
    # driver.find_element_by_id("ww").send_keys(Keys.CONTROL+'a')
    # driver.find_element_by_id("ww").send_keys(Keys.BACKSPACE)
    #执行点击鼠标右键
    # ele=driver.find_element_by_xpath("//div/a/img[@alt='百度新闻']")
    # actionChain=ActionChains(driver)
    #此操作可点击鼠标右键，可分多个步骤执行，.perform()执行缓存的步骤
    # actionChain.context_click(ele).perform()
    #（不能实现）此行代码想实现点击鼠标右键之后，再用方向键调节右键菜单中的光标，并点击菜单的功能，但是没实现
    # actionChain.context_click(ele).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    #执行javascript脚本（弹出一个弹框）
    #driver.execute_script("window.alert('这是一个alart弹框。');")
    #执行js脚本来控制浏览器竖向滚动条.打开百度贴吧，然后拖动滚动条到左侧 “地区"
    # driver.get("https://tieba.baidu.com/index.html")
    # sleep(5)
    # ele=driver.find_element_by_link_text("地区")
    # driver.execute_script("return arguments[0].scrollIntoView();",ele)
    #切换窗口
    # driver.find_element_by_xpath("//div[@id='pane-news']/div/ul/li[1]/strong/a").click()#news.baidu.com
    # sleep(5)
    # print(driver.current_window_handle)#输入当前窗口句柄
    # handles=driver.window_handles#获取当前全部窗口句柄合集
    # print(handles)#输出句柄合集
    # for handle in handles:#切换窗口(当前窗口在handles中为第一个窗口)
    #     if handle!=driver.current_window_handle:#当查询到handles中第二个的时候，才进行切换窗口操作
    #         print("switch to second window",handle)
    #         driver.close()#关闭第一个窗口
    #         sleep(3)
    #         driver.switch_to_window(handle)#切换到第二个窗口
    #判断新页面的标题是否上个页面点击的链接
    # ele=driver.find_element_by_xpath("//div[@id='pane-news']/div/ul/li[1]/strong/a")
    # link_str=ele.text
    # print(link_str)
    # ele.click()
    # sleep(5)
    # handles=driver.window_handles
    # for handle in handles:
    #     if handle!=driver.current_window_handle:
    #         driver.switch_to_window(handle)
    # page2_title_str=driver.find_element_by_xpath("//*[@id='conTit']/h1").text#获取目标元素的text
    # print(page2_title_str)
    # assert link_str in page2_title_str
    #多表单切换（heml界面中很少有仅有一个表单的，测试中需要在多个表单中进行切换）
    # driver.get("C:\\Users\\wangjf\\Desktop\\new1.html")
    # driver.switch_to.frame("frame1")#切换到id为frame1的表单中
    #切换完成之后，里面的元素操作就可以直接用driver操作
    # driver.find_element_by_xpath("//*/input[@id='kw']").send_keys("selenium")
    #操作完成之后，重新切回默认的网页（表单），才能再次切换为下一个表单
    # driver.switch_to_default_content()
    #切换进入下个表单
    # driver.switch_to.frame("frame2")
    # driver.find_element_by_link_text('More information...').click()
    #进行元素操作之后再次切回初始表单
    # driver.switch_to_default_content()
    driver.get("https://pypi.python.org/simple/")
    sleep(5)
    driver.find_element_by_link_text("ply").click()
    sleep(10)

    print("Test pass")
    sleep(10)

except Exception as e:
    print("Assertion test Fail!Exception message:",format(e))
# driver.quit()

