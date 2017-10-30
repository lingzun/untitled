#!/usr/bin/env python3
#coding:utf-8

import configparser
import os
class ReadConfigFile(object):
    def get_value(self):
        root_dir = os.path.dirname(os.path.abspath('.'))#获取项目根目录的绝对路径
        print (root_dir)

        config=configparser.ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)
        browser=config.get("browserType","browserName")
        url=config.get("testServer","URL")

        return(browser,url)#返回的是一个元组
trcf=ReadConfigFile()
print(trcf.get_value())

