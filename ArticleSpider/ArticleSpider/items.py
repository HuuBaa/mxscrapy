# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy, re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join, Compose
from datetime import datetime


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def date_convert(value):
    value = value.strip().replace('·', '').strip()
    try:
        create_date = datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.now().date()
    return create_date


def get_nums(value):
    re_match = re.match(r'.*?(\d+).*', value)
    value = int(re_match.group(1)) if re_match else 0
    return value


def remove_comment_tags(value):
    # 去掉提取的tag中的评论
    return "" if "评论" in value else value


def return_value(value):
    return value


class ArticleItemLoader(ItemLoader):
    # 自定义itemloader
    default_output_processor = TakeFirst()


class JobboleArtileItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert)
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    front_image_path = scrapy.Field()
    like_num = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comment_num = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    fav_num = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    content = scrapy.Field()
    tags = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join(',')
    )

    def get_insert_sql(self):
        insert_sql = """
                    INSERT INTO jobbolearticle(
                            title,
                            create_date,
                            url,
                            url_object_id,
                            front_image_url,
                            front_image_path,
                            like_num,
                            comment_num,
                            fav_num,
                            content,
                            tags) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
                    """
        params = (
            self['title'], self['create_date'], self['url'], self['url_object_id'], self['front_image_url'][0],
            self['front_image_path'], self['like_num'], self['comment_num'], self['fav_num'], self['content'],
            self['tags']
        )

        return insert_sql, params


class ZhihuQuestionItem(scrapy.Item):
    zhihu_id = scrapy.Field()
    title = scrapy.Field()
    topics = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    comment_num = scrapy.Field()
    watch_num = scrapy.Field()
    view_num = scrapy.Field()
    answer_num = scrapy.Field()
    crawl_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """ 
            INSERT INTO zhihu_question(              
              `zhihu_id`,
              `title`,
              `topics`, 
              `url`,
              `content`, 
              `comment_num`,
              `watch_num`, 
              `view_num`, 
              `answer_num`,
              `crawl_time`
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE 
              `content`=VALUES(`content`),
              `comment_num`=VALUES(`comment_num`),
              `watch_num`=VALUES(`watch_num`),
              `answer_num`=VALUES(`answer_num`),
              `view_num`=VALUES(`view_num`),
              `crawl_time`=VALUES(`crawl_time`);
        """

        zhihu_id = self['zhihu_id'][0]
        title = self['title'][0]
        topics = ','.join(self['topics'])
        url = self['url'][0]
        content = ''.join(self['content'])
        comment_num = get_nums(self['comment_num'][0])
        watch_num =''.join(self['watch_num'][0].split(','))
        view_num = ''.join(self['view_num'][0].split(','))
        answer_num = ''.join(self['answer_num'][0].split(',')) if 'answer_num' in self else 0
        crawl_time = self['crawl_time'][0]

        params = (
            zhihu_id,title,topics,url,content,comment_num,watch_num,view_num,answer_num,crawl_time
        )

        return insert_sql, params


class ZhihuAnswerItem(scrapy.Item):
    zhihu_id = scrapy.Field()
    question_id = scrapy.Field()
    author_id = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    comment_num = scrapy.Field()
    praise_num = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    crawl_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """ 
            INSERT INTO  zhihu_answer(
              `zhihu_id`,
              `question_id`,
              `author_id`,
              `url`,
              `content`,
              `comment_num`,
              `praise_num`,
              `create_time`,
              `update_time`,
              `crawl_time`
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE 
              `content`=VALUES (`content`),
              `comment_num`=VALUES (`comment_num`),
              `update_time`=VALUES (`update_time`),
              `praise_num`=VALUES (`praise_num`),
              `crawl_time`=VALUES (`crawl_time`)                 
        """
        params=(
            self['zhihu_id'],self['question_id'],self['author_id'],self['url'],self['content'],self['comment_num'],self['praise_num'],self['create_time'],self['update_time'],self['crawl_time'],
        )

        return insert_sql, params
