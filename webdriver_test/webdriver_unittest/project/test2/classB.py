# -*- coding: utf-8 -*-

import sys
sys.path.append('D:/workspace/webdriver_test/webdriver_unittest/project/')
from test1.classA import ClassA


class ClassB(ClassA):

    def test_inherit(self):
        self.open_baidu()

test = ClassB()
test.test_inherit()