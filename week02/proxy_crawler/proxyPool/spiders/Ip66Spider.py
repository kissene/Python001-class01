# -*- coding: utf-8 -*-

import logging
from lxml import etree

from week02.proxy_crawler.config.config import get_log_config
from week02.proxy_crawler.proxyPool.model.proxy import Proxy
from week02.proxy_crawler.proxyPool.spiders.baseSpider import BaseSpider

'''
    66ip 爬虫
@Author kissene_xie
@Date 20200704
'''

from fake_useragent import UserAgent
class Ip66Spider(BaseSpider):

    url = 'http://www.66ip.cn/areaindex_1/1.html'

    agent = "66ip"
    user_a = UserAgent()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'http://www.66ip.cn/areaindex_1/1.html',
        'Content-Type': 'text/html;charset=UTF-8',
        'Cache-Control': 'no-cache',
        'Host': 'www.66ip.cn',
        'User-Agent': user_a.random,
    }

    @classmethod
    def get_proxies(self):
        # 加载 Log 配置
        get_log_config()

        proxy_model_list = []

        print('正在爬取66ip……')

        response = super(Ip66Spider, self).get_proxies()
        selector = etree.HTML(response.text)

        infos = selector.xpath('//*[@id="footer"]/div/table//tr')
        tmp_infos = infos[1:]

        for i, info in enumerate(tmp_infos):
            try:
                ip = info.xpath('//td[1]/text()')[i]               # ip
                port = info.xpath('//td[2]/text()')[i]             # 端口
                anonymity = ''      # 匿名度
                http_type = info.xpath('//td[4]/text()')[i]             # 类型
                area = info.xpath('//td[3]/text()')[i]       # 地区, 省
                area = ''  # 地区, 市
                speed = ''            # 速度

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
