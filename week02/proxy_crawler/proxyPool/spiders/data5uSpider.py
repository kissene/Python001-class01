# -*- coding: utf-8 -*-

import logging
from lxml import etree

from week02.proxy_crawler.config.config import get_log_config
from week02.proxy_crawler.proxyPool.model.proxy import Proxy
from week02.proxy_crawler.proxyPool.spiders.baseSpider import BaseSpider

'''
    无忧代理(data5u) 爬虫
@Author monkey
@Date 2017-12-18
'''

from fake_useragent import UserAgent
class Data5uSpider(BaseSpider):

    url = 'http://www.data5u.com'

    agent = "data5u"
    user_a = UserAgent()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'http://www.data5u.com',
        'Content-Type': 'text/html;charset=UTF-8',
        'Cache-Control': 'no-cache',
        'Host': 'www.data5u.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': user_a.random,
    }

    @classmethod
    def get_proxies(self):
        # 加载 Log 配置
        get_log_config()

        proxy_model_list = []

        print('正在爬取无忧代理……')

        response = super(Data5uSpider, self).get_proxies()
        selector = etree.HTML(response.text)

        infos = selector.xpath('//ul[@class="l2"]')

        for i, info in enumerate(infos):
            try:
                ip = info.xpath('//ul[@class="l2"]/span[1]/li/text()')[i]               # ip
                port = info.xpath('//ul[@class="l2"]/span[2]/li/text()')[i]             # 端口
                anonymity = info.xpath('//ul[@class="l2"]/span[3]/li/text()')[i]      # 匿名度
                http_type = info.xpath('//ul[@class="l2"]/span[4]/li/text()')[i]           # 类型
                area = info.xpath('//ul[@class="l2"]/span[5]/li/text()')[i]        # 地区, 省
                area = area + info.xpath('//ul[@class="l2"]/span[6]/li/text()')[i]  # 地区, 市
                speed = info.xpath('//ul[@class="l2"]/span[8]/li/text()')[i]            # 速度

                print(ip + " | " + port + " | " + anonymity + " | " + http_type + " | " + area + " | " + speed + " | ")

                if http_type == 'http' or http_type == 'https':
                    # print(http_type + "://" + ip + ":" + port)
                    proxy = Proxy()
                    proxy.set_ip(ip)
                    proxy.set_port(port)
                    proxy.set_http_type(http_type)
                    proxy.set_anonymity(anonymity)
                    proxy.set_area(area)
                    proxy.set_speed(speed)
                    proxy.set_agent(self.agent)
                    proxy.set_survival_time("")
                    proxy_model_list.append(proxy)
                else:
                    pass
            except Exception as e:
                logging.debug(e)

        logging.debug("抓取 " + self.agent + " 网站共计 " + str(len(proxy_model_list)) + " 个代理")

        return proxy_model_list
