# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/6/29 20:21'

import re
line="你2w3好"
regex_str="(你\w+好)"
match_obj=re.match(regex_str,line)
if match_obj:
    print(match_obj .groups())

