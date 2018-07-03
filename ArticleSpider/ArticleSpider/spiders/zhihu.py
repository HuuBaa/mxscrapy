# -*- coding: utf-8 -*-
import scrapy
from ..utils.zhihu_login_req import headers,cookies

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        print(response.text)
        yield scrapy.Request('https://www.zhihu.com/people/edit',callback=self.cab,headers=headers)

    def cab(self,response):
        pass

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True,headers=headers,cookies=cookies)


