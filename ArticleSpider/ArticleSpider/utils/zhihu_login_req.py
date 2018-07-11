# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/7/3 12:56'

import requests, re
from http import cookiejar
from http.cookies import  SimpleCookie

Cookie='q_c1=a52e9a125f534fa384a260ec49a67157|1531016901000|1495874677000; _ga=GA1.2.252382496.1492062036; d_c0="ABBCiH2pmguPTjhRrwkIE7TFCfQJADEQEjM=|1492137756"; _zap=54ac052b-364b-4717-bca2-928d0af8089a; __utma=155987696.252382496.1492062036.1530764312.1530764312.1; __utmz=155987696.1530764312.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); q_c1=a52e9a125f534fa384a260ec49a67157|1506558012000|1495874677000; __DAYU_PP=qIBV6rzYbNZEnq273bu22daae279ccb6; capsion_ticket="2|1:0|10:1531016890|14:capsion_ticket|44:MTY3MDQ0NDNlM2I5NDY4YmE1NzI5MzljNmNlOTczYjE=|815c1c28532534a198912c712487966f5e60afc360cfae2c5895b6278465aa1e"; r_cap_id="YmQ5YTIzNGE4YzJmNDU0Nzk4MjhjMjExODUwYjRiN2U=|1530606330|4105f92253443c16019f612071ca7696c4c1fbc5"; cap_id="OTdmZjE1ZmIwNGZmNGU4OGEyYjI0MGUyZjFmZTAwNzA=|1530606330|cffe41ae483ca21342c58ea5de9fba84bfbdbcd6"; l_cap_id="NDQ0MDhmZWQ1NTQyNDhhM2JkNzY1MjFmMTUwNjYyYjU=|1530606330|cc213d269cae29cc6c716f3b734ccd0b9f22d944"; _xsrf=xddUYUkNq0Mv4xLnwofPHXF76tz0gljE; tgw_l7_route=29b95235203ffc15742abb84032d7e75; z_c0="2|1:0|10:1531016898|4:z_c0|92:Mi4xWndUd0FRQUFBQUFBRUVLSWZhbWFDeVlBQUFCZ0FsVk53c1F1WEFDRXNXWWJmUWtWMU5aX2lVMnJvSHZDVHd4dGV3|7176a106fed88edac7c4b9b4cc4b2b1e65aed01edc277785fdab3774d88d9722"'

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
