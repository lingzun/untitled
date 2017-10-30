#!/usr/bin/env python3
#coding:utf-8
import time
from test1.browser_engine import BrowserEngine
class TestBrowser(object):
    def open_browser(self):
        brow=BrowserEngine(self)
        driver=brow.get_browser()
tbe=TestBrowser()
tbe.open_browser()


