# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/7/2 16:50'

import hashlib

def get_md5(url):
    if isinstance(url,str):
        url=url.encode('utf-8')
    m=hashlib.md5()
    m.update(url)
    return m.hexdigest()

