# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/7/3 12:56'

import requests, re
from http import cookiejar
from http.cookies import  SimpleCookie

Cookie='q_c1=a52e9a125f534fa384a260ec49a67157|1530606336000|1495874677000; _ga=GA1.2.252382496.1492062036; d_c0="ABBCiH2pmguPTjhRrwkIE7TFCfQJADEQEjM=|1492137756"; _zap=54ac052b-364b-4717-bca2-928d0af8089a; __utma=51854390.252382496.1492062036.1528001597.1528001597.1; __utmz=51854390.1528001597.1.1.utmcsr=blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/xys430381_1/article/details/77891461; q_c1=a52e9a125f534fa384a260ec49a67157|1506558012000|1495874677000; __DAYU_PP=qIBV6rzYbNZEnq273bu22daae279ccb6; __utmv=51854390.100--|2=registration_date=20150803=1^3=entry_date=20150803=1; _xsrf=84872bce-64c9-4035-963c-0cd2f4f2867a; capsion_ticket="2|1:0|10:1530606332|14:capsion_ticket|44:MTI2Y2ZkODMwNTI0NDgwMTk5ZWYwMWY2NWFhZDk0YzA=|92500e9e841b7b77f379c8751384b11d554644560768c61b279929bea2df6723"; l_n_c=1; r_cap_id="YmQ5YTIzNGE4YzJmNDU0Nzk4MjhjMjExODUwYjRiN2U=|1530606330|4105f92253443c16019f612071ca7696c4c1fbc5"; cap_id="OTdmZjE1ZmIwNGZmNGU4OGEyYjI0MGUyZjFmZTAwNzA=|1530606330|cffe41ae483ca21342c58ea5de9fba84bfbdbcd6"; l_cap_id="NDQ0MDhmZWQ1NTQyNDhhM2JkNzY1MjFmMTUwNjYyYjU=|1530606330|cc213d269cae29cc6c716f3b734ccd0b9f22d944"; n_c=1; tgw_l7_route=4902c7c12bebebe28366186aba4ffcde; z_c0="2|1:0|10:1530606334|4:z_c0|92:Mi4xWndUd0FRQUFBQUFBRUVLSWZhbWFDeVlBQUFCZ0FsVk5fWUFvWEFEMGNyR0ROb0N3MGtSZ1ZfRGkyZ0ZTQzlEWmhn|8c206e1d0e5fa736d1d575fe917a36a772b0703f64407386971c2d5033131cf5"'

#cookie字符串转dict
cookie=SimpleCookie()
cookie.load(Cookie)
cookies = {}
for key, morsel in cookie.items():
    cookies[key] = morsel.value

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}

headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie': 'q_c1=a52e9a125f534fa384a260ec49a67157|1530606336000|1495874677000; _ga=GA1.2.252382496.1492062036; d_c0="ABBCiH2pmguPTjhRrwkIE7TFCfQJADEQEjM=|1492137756"; _zap=54ac052b-364b-4717-bca2-928d0af8089a; __utma=51854390.252382496.1492062036.1528001597.1528001597.1; __utmz=51854390.1528001597.1.1.utmcsr=blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/xys430381_1/article/details/77891461; q_c1=a52e9a125f534fa384a260ec49a67157|1506558012000|1495874677000; __DAYU_PP=qIBV6rzYbNZEnq273bu22daae279ccb6; __utmv=51854390.100--|2=registration_date=20150803=1^3=entry_date=20150803=1; _xsrf=84872bce-64c9-4035-963c-0cd2f4f2867a; capsion_ticket="2|1:0|10:1530606332|14:capsion_ticket|44:MTI2Y2ZkODMwNTI0NDgwMTk5ZWYwMWY2NWFhZDk0YzA=|92500e9e841b7b77f379c8751384b11d554644560768c61b279929bea2df6723"; l_n_c=1; r_cap_id="YmQ5YTIzNGE4YzJmNDU0Nzk4MjhjMjExODUwYjRiN2U=|1530606330|4105f92253443c16019f612071ca7696c4c1fbc5"; cap_id="OTdmZjE1ZmIwNGZmNGU4OGEyYjI0MGUyZjFmZTAwNzA=|1530606330|cffe41ae483ca21342c58ea5de9fba84bfbdbcd6"; l_cap_id="NDQ0MDhmZWQ1NTQyNDhhM2JkNzY1MjFmMTUwNjYyYjU=|1530606330|cc213d269cae29cc6c716f3b734ccd0b9f22d944"; n_c=1; tgw_l7_route=4902c7c12bebebe28366186aba4ffcde; z_c0="2|1:0|10:1530606334|4:z_c0|92:Mi4xWndUd0FRQUFBQUFBRUVLSWZhbWFDeVlBQUFCZ0FsVk5fWUFvWEFEMGNyR0ROb0N3MGtSZ1ZfRGkyZ0ZTQzlEWmhn|8c206e1d0e5fa736d1d575fe917a36a772b0703f64407386971c2d5033131cf5"'
}

res = requests.get("https://www.zhihu.com/", headers=headers1)

with open('i.html', 'w', encoding='utf-8') as f:
    f.write(res.text)

print(res.text)
