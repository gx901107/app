# -*- coding: utf-8 -*-
# @Time : 2020/12/20 21:48
# @Author : nichao
# @Email : 530504026@qq.com
# @File : run.py
# @Project : appAuto
from BeautifulReport import BeautifulReport
import time
import unittest
discover=unittest.defaultTestLoader.discover('./case','search.py')
BeautifulReport(discover).report(description="自动化测试报告",report_dir='./report',
                          filename=time.strftime("%Y-%m-%d %H_%M_%S"))
