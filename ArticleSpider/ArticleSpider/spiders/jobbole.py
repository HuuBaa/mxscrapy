# -*- coding: utf-8 -*-
import scrapy,re
from datetime import datetime
from scrapy.http import Request
from urllib import parse
from scrapy.loader import ItemLoader
from selenium import webdriver
from scrapy import signals
from pydispatch import dispatcher

from ..items import JobboleArtileItem,ArticleItemLoader
from ..utils.common import get_md5

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    #selenium支持
    # def __init__(self,**kwargs):
    #     self.browser=webdriver.Firefox()
    #     super(JobboleSpider,self).__init__()
    #     dispatcher.connect(self.spider_closed,signals.spider_closed)
    #
    # #信号量
    # def spider_closed(self):
    #     print("spider close")
    #     self.browser.quit()

    def parse(self, response):
        post_nodes=response.css('div#archive .floated-thumb .post-thumb a')
        for post_node in post_nodes:
            image_url=post_node.css('img::attr(src)').extract_first("")
            post_url=post_node.css('::attr(href)').extract_first("")
            yield Request(url=parse.urljoin(response.url,post_url),meta={"front_image_url":parse.urljoin(response.url,image_url)},callback=self.parse_detail)

        #提取下一页
        next_url=response.css('.next.page-numbers::attr(href)').extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url,next_url), callback=self.parse)


    def parse_detail(self,response):
        # title=response.xpath('//div[@class="entry-header"]/h1/text()').extract_first()
        # create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract_first().strip()[:-1].strip()
        # like_num=response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract_first()
        #
        # fav_num =response.css('span.bookmark-btn::text').extract_first()
        # re_fav_num = re.match(r'.*?(\d+).*', fav_num)
        # fav_num = int(re_fav_num.group(1)) if re_fav_num else 0
        #
        # comment_num=response.xpath('//a[@href="#article-comment"]/span/text()').extract_first()
        # re_comment_num=re.match(r'.*?(\d+).*',comment_num)
        # comment_num=int(re_comment_num.group(1)) if re_comment_num else 0
        #
        # content=response.xpath('//div[@class="entry"]').extract_first()
        #
        # tag_list=response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        # tag_list=[el for el in tag_list if not el.strip().endswith("评论")]
        # tags=','.join(tag_list)

        #css
        # article_item=JobboleArtileItem()
        #
        # front_image_url=response.meta.get("front_image_url","")
        # title = response.css('.entry-header h1::text').extract_first()
        # create_date = response.css('p.entry-meta-hide-on-mobile::text').extract_first().strip().replace('·', '').strip()
        # like_num =  response.css('span.vote-post-up h10::text').extract_first()
        #
        # fav_num = response.css('span.bookmark-btn::text').extract_first()
        # re_fav_num = re.match(r'.*?(\d+).*', fav_num)
        # fav_num = int(re_fav_num.group(1)) if re_fav_num else 0
        #
        # comment_num =  response.css('a[href="#article-comment"] span::text').extract_first()
        # re_comment_num = re.match(r'.*?(\d+).*', comment_num)
        # comment_num = int(re_comment_num.group(1)) if re_comment_num else 0
        #
        # content = response.css('div.entry').extract_first()
        #
        # tag_list = response.css('p.entry-meta-hide-on-mobile a::text').extract()
        # tag_list = [el for el in tag_list if not el.strip().endswith("评论")]
        # tags = ','.join(tag_list)
        #
        # article_item["title"]=title
        # article_item["url"] = response.url
        # article_item["url_object_id"] = get_md5(response.url)
        # try:
        #     create_date=datetime.strptime(create_date,"%Y/%m/%d").date()
        # except Exception as e:
        #     create_date=datetime.now().date()
        # article_item["create_date"] = create_date
        # article_item["like_num"] = like_num
        # article_item["fav_num"] = fav_num
        # article_item["comment_num"] = comment_num
        # article_item["content"] = content
        # article_item["tags"] = tags
        # article_item["front_image_url"] = [front_image_url]

        #通过ItemLoader加载item

        front_image_url = response.meta.get("front_image_url", "")
        item_loader=ArticleItemLoader(item=JobboleArtileItem(),response=response)

        item_loader.add_css('title','.entry-header h1::text')
        item_loader.add_value('url', response.url)
        item_loader.add_value('url_object_id', get_md5(response.url))
        item_loader.add_css('create_date','p.entry-meta-hide-on-mobile::text')
        item_loader.add_value('front_image_url', [front_image_url])
        item_loader.add_css('like_num', 'span.vote-post-up h10::text')
        item_loader.add_css('fav_num', 'span.bookmark-btn::text')
        item_loader.add_css('comment_num', 'a[href="#article-comment"] span::text')
        item_loader.add_css('content', 'div.entry')
        item_loader.add_css('tags', 'p.entry-meta-hide-on-mobile a::text')

        article_item=item_loader.load_item()

        #会传递到pipline
        yield article_item


