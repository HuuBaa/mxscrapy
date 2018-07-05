# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/7/3 12:56'

import requests, re
from http import cookiejar
from http.cookies import  SimpleCookie

Cookie='q_c1=a52e9a125f534fa384a260ec49a67157|1530716477000|1495874677000; _ga=GA1.2.252382496.1492062036; d_c0="ABBCiH2pmguPTjhRrwkIE7TFCfQJADEQEjM=|1492137756"; _zap=54ac052b-364b-4717-bca2-928d0af8089a; __utma=51854390.252382496.1492062036.1530715886.1530715886.1; __utmz=51854390.1530715886.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; q_c1=a52e9a125f534fa384a260ec49a67157|1506558012000|1495874677000; __DAYU_PP=qIBV6rzYbNZEnq273bu22daae279ccb6; capsion_ticket="2|1:0|10:1530716468|14:capsion_ticket|44:NmRhYzA5ZTY5MGUwNDRlZjg3ZDA2MDE2NjRmOTUzNzY=|e8e976ead65b261648e044ff1f134cf0b2ca3ae2e140a4b9c5309e6b3ffdcb86"; r_cap_id="YmQ5YTIzNGE4YzJmNDU0Nzk4MjhjMjExODUwYjRiN2U=|1530606330|4105f92253443c16019f612071ca7696c4c1fbc5"; cap_id="OTdmZjE1ZmIwNGZmNGU4OGEyYjI0MGUyZjFmZTAwNzA=|1530606330|cffe41ae483ca21342c58ea5de9fba84bfbdbcd6"; l_cap_id="NDQ0MDhmZWQ1NTQyNDhhM2JkNzY1MjFmMTUwNjYyYjU=|1530606330|cc213d269cae29cc6c716f3b734ccd0b9f22d944"; _xsrf=4ef3bd5f-2740-4776-bf4c-e12f10c1edb7; __utmb=51854390.0.10.1530715886; __utmc=51854390; __utmv=51854390.100--|2=registration_date=20150803=1^3=entry_date=20150803=1; tgw_l7_route=56f3b730f2eb8b75242a8095a22206f8; z_c0="2|1:0|10:1530716471|4:z_c0|92:Mi4xWndUd0FRQUFBQUFBRUVLSWZhbWFDeVlBQUFCZ0FsVk5OeThxWEFDVjNyOEdSaFhqN2FPdjFVVlR3MTlYSV9YYk5B|9e03a4654407df8211aad949b4241440ff83c791716d28ae1053e6e358f4b119"'

#cookie字符串转dict
cookie=SimpleCookie()
cookie.load(Cookie)
cookies = {}
for key, morsel in cookie.items():
    cookies[key] = morsel.value

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}

if __name__=="main":
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Cookie': Cookie
    }

    res = requests.get("https://www.zhihu.com/", headers=headers1)

    with open('i.html', 'w', encoding='utf-8') as f:
        f.write(res.text)

    print(res.text)
