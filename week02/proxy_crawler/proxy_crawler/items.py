# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyCrawlerItem(scrapy.Item):
    # 电影名称
    name = scrapy.Field()
    # 电影类型
    type = scrapy.Field()
    # 上映时间
    time = scrapy.Field()
