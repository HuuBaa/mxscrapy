# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/110287/']

    def parse(self, response):
        title=response.xpath('//*[@id="post-110287"]/div[1]/h1/text()').extract()[0]
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip()[:-1].strip()
        like_num=response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0]

        fav_num=re.match(
            r'.*?(\d+).*',
            response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]
        ).group(1)

        comment_num=re.match(
            r'.*?(\d+).*',
            response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]
        ).group(1)

        content=response.xpath('//div[@class="entry"]').extract()[0]

        tag_list=response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list=[el for el in tag_list if not el.strip().endswith("评论")]
        tag=','.join(tag_list)

        pass
