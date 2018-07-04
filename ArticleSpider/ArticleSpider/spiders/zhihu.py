# -*- coding: utf-8 -*-
import scrapy,re,json
from urllib import parse
from datetime import datetime

from scrapy.loader import ItemLoader
from ..utils.zhihu_login_req import headers,cookies
from ..items import ZhihuQuestionItem,ZhihuAnswerItem

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    answer_url="https://www.zhihu.com/api/v4/questions/{0}/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].mark_infos[*].url;data[*].author.follower_count,badge[?(type=best_answerer)].topics&limit={1}&offset={2}&sort_by=default"

    def start_requests(self):
        for url in self.start_urls:
            # 带上cookie登录
            yield scrapy.Request(url, dont_filter=True, headers=headers, cookies=cookies)

    def parse(self, response):
        #获取主页的所有url
        all_urls=response.css('a::attr(href)').extract()
        all_urls=[parse.urljoin(response.url,url) for url in all_urls]
        all_urls=list(filter(lambda x:x.startswith('https'),all_urls))
        for url in all_urls:
            #找出question类型的url
            re_match=re.match(r'(.*zhihu.com/question/(\d+))(/|$).*',url)
            if re_match:
                question_url=re_match.group(1)
                yield scrapy.Request(question_url,callback=self.parse_question,headers=headers)
            else:
                yield scrapy.Request(url,callback=self.parse,headers=headers)

    def parse_question(self,response):
        item_loader = ItemLoader(item=ZhihuQuestionItem(), response=response)
        re_match = re.match(r'(.*zhihu.com/question/(\d+))(/|$).*', response.url)
        if re_match:
            question_id = re_match.group(2)
            item_loader.add_value('zhihu_id',question_id)
            item_loader.add_value('url', response.url)
            item_loader.add_css('title','h1.QuestionHeader-title::text')
            item_loader.add_css('topics','.QuestionTopic .Popover div::text')
            item_loader.add_css('content','.QuestionHeader-detail')
            item_loader.add_css('comment_num','.QuestionHeader-Comment button::text')
            item_loader.add_css('answer_num','.List-header .List-headerText span::text')
            item_loader.add_css('watch_num','.QuestionFollowStatus div button div strong::text')
            item_loader.add_css('view_num', '.QuestionFollowStatus div div div strong::text')
            item_loader.add_value('crawl_time',datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            question_item=item_loader.load_item()

            yield scrapy.Request(self.answer_url.format(question_id,20,0),headers=headers,callback=self.parse_answer)
            yield question_item

    def parse_answer(self,response):
        answer_dict=json.loads(response.text)
        is_end=answer_dict['paging']['is_end']
        next_url=answer_dict['paging']['next']
        if answer_dict['data'] is not []:
            for answer in answer_dict['data']:
                answer_item=ZhihuAnswerItem()
                answer_item['zhihu_id']=answer['id']
                answer_item['url'] = answer['url']
                answer_item['question_id'] = answer['question']['id']
                answer_item['author_id'] ="匿名用户" if answer['author']['id'] =="0" else answer['author']['id']
                answer_item['content'] = answer['content'] if 'content' in answer else ""
                answer_item['update_time'] = answer['updated_time']
                answer_item['create_time'] = answer['created_time']
                answer_item['comment_num'] = answer['comment_count']
                answer_item['praise_num'] = answer['voteup_count']
                answer_item['crawl_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                yield answer_item

            if not is_end:
                yield scrapy.Request(next_url,headers=headers,callback=self.parse_answer)





