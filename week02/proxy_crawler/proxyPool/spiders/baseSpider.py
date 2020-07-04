# -*- coding: utf-8 -*-





'''
    爬虫的基类
@Author monkey
@Date 2017-12-17
'''

from week02.proxy_crawler.proxyPool.requester import requestEnginer


class BaseSpider(object):

    url = ""

    headers = {}

    def __init__(self):
        pass

    '''
    解析爬取结果
    '''
    @classmethod
    def get_proxies(self):
        if self.headers is None:
            response = requestEnginer.do_get(self.url)
        else:
            response = requestEnginer.do_get(self.url, self.headers)
        return response
