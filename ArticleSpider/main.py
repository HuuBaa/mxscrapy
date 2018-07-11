# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/7/1 18:50'

from scrapy.cmdline import execute
import sys,os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(["scrapy","crawl","jobbole"])
# execute(["scrapy","crawl","zhihu"])