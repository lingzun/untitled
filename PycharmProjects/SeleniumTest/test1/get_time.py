#!/usr/bin/env python3
#coding:utf-8
import time
class GetTime(object):
    def get_sys_time(self):
        print(time.time())#获取从1970到现在的时间间隔（单位为秒）
        print(time.localtime())
        # now_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())#格式化时间，按照年-月-日 时：分：秒的格式打印出来
        now_time=time.strftime("%Y/%m/%d %H:%M:%S",time.localtime())#格式化时间，按照年/月/日 时：分：秒的格式打印出来
        print(now_time)
strf=GetTime()
strf.get_sys_time()