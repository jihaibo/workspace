# -*- coding: utf-8 -*-

import time
from BrowserEngine import browser_engine

class TestBrowserEngine(object):

    def open_browser(self):
        browserengine = browser_engine.BrowserEngine(self)
        driver = browserengine.get_browser()

tbe = TestBrowserEngine()
tbe.open_browser()

