# -*- coding: utf-8 -*-

import ConfigParser
import os

class TestReadConfigFile(object):

    def get_value(self):
        root_dir = os.path.dirname(os.path.abspath('.')) #获取项目根目录的相对路径
        print root_dir

        config = ConfigParser.ConfigParser()
        file_path = root_dir + '/project/config/cofig.ini'
        config.read(file_path)

        browser = config.get("browserType","browserName")
        url = config.get("testServer","URL")

        return(browser,url)

trcf = TestReadConfigFile()
print trcf.get_value()