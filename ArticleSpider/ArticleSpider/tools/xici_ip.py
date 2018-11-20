# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/7/7 20:30'
import requests, json, re
from scrapy.selector import Selector
import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="password", db="mxscrapy", charset="utf8")
cursor = conn.cursor()


def crawl_xici():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    for i in range(1, 3283):

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
                    ip_info[0], ip_info[1], ip_info[2], ip_info[3]
                )
            )
            conn.commit()


# crawl_xici()

class GetProxyIp(object):
    def get_proxy_ip(self):
        """
        #随机获取一个代理ip
        :return:
        """
        sql = "SELECT proxy FROM ips ORDER BY RAND() LIMIT 1;"
        cursor.execute(sql)
        proxy_ip = cursor.fetchone()[0]
        if self.verify_proxy_ip(proxy_ip):
            return proxy_ip
        else:
            return self.get_proxy_ip()

    def verify_proxy_ip(self, proxy_ip):
        """
        验证代理ip
        :param proxy_ip:
        :return:
        """
        proxies = {
            'http': proxy_ip,
        }
        print("正在进行代理ip：" + proxy_ip + "的验证...")
        try:
            res = requests.get("http://icanhazip.com/", proxies=proxies, timeout=5)
        except Exception as e:
            self.delete_proxy_ip(proxy_ip)
            return False
        else:
            re_match = re.match(r'(https|http)://([\d\.]*):\d+', proxy_ip)
            if res.status_code==200 and res.text.strip() == re_match.group(2):
                print("获取到可用ip："+proxy_ip)
                return True
            else:
                self.delete_proxy_ip(proxy_ip)
                return False

    def delete_proxy_ip(self, proxy_ip):
        """
        删除无效的ip
        :param proxy_ip:
        :return:
        """
        sql="DELETE FROM ips WHERE proxy='{0}'".format(proxy_ip)
        cursor.execute(sql)
        conn.commit()
        print('删除了无效ip：{0}'.format(proxy_ip))



ip=GetProxyIp().get_proxy_ip()

proxies = {
      'https': ip,
    }
res=requests.get("https://5iittt.bid/intr/ff7e4a4131a739b3", proxies=proxies)
print(res)




def get_ip_json_list():
    # 获取代理ip
    res = requests.get("https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list")

    with open("ips.json", "wb") as f:
        f.write(res.text.encode("utf8"))

def json_2_dict():
    # 从json文件一行行读取=>dict
    ip_dicts = []
    with open("ips.json", "r") as f:
        for line in f.readlines():
            ip_dicts.append(json.loads(line))
    return ip_dicts


def dict_2_mysql(ip_dicts):
    # ip_dicts格式化代理地址
    ip_list = []
    for ip_dict in ip_dicts:
        ip_list.append(
            "{type}://{host}:{port}".format(type=ip_dict['type'], host=ip_dict['host'], port=ip_dict['port']))

    # 写入到txt文件
    # with open("ips.txt", "w") as f:
    #     f.writelines(ip_list)

    # 保存到mysql
    for ip in ip_list:
        sql = "INSERT ignore INTO  ips(`proxy`) VALUES ('{0}')".format(ip)
        cursor.execute(sql)
        conn.commit()

#获取新ip时使用
# get_ip_json_list()
# dict_2_mysql(json_2_dict())


