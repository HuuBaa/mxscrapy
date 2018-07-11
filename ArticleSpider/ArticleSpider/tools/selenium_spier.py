# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/7/9 9:31'

from selenium import webdriver
from scrapy import Selector

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

# 不加载图片
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

#无界面模式
# options.add_argument("--headless")
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=options)

driver.get("https://www.ioboom.com")
t_selector = Selector(text=driver.page_source)
title = t_selector.css("title")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

print(title)
#driver.quit()
