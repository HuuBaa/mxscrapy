# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/7/7 20:30'
import requests
from scrapy.selector import Selector
import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="password", db="mxscrapy", charset="utf8")
cursor = conn.cursor()

def crawl_xici():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    for i in range(1,3283):

        res = requests.get("http://www.xicidaili.com/nn/{0}".format(i), headers=headers)
        print(res.url)
        selector = Selector(text=res.text)
        all_trs = selector.css("#ip_list tr")
        ip_list = []
        for tr in all_trs[1:]:

            speed_str = tr.css(".bar::attr(title)").extract_first()  # 6.377秒
            if speed_str:
                speed = float(speed_str.split("秒")[0])
                all_texts = tr.css("td::text").extract()
                ip = all_texts[0]
                port = all_texts[1]
                proxy_type = all_texts[-7]
                ip_list.append((ip, port, proxy_type, speed))

        for ip_info in ip_list:
            cursor.execute(
                "INSERT ignore proxy_ips(`ip`,`port`,`proxy_type`,`speed`) VALUES('{0}','{1}','{2}','{3}')".format(
                    ip_info[0],ip_info[1],ip_info[2],ip_info[3]
                )
            )
            conn.commit()

# crawl_xici()
