# ****************************
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 20:23
# Author = kissene_xie
# @File    : user_agent_middlewares
# ****************************
__author__ = 'kissene_xie'


from week01.utils.get_user_agent_setting import get_setting


class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        header_config = get_setting()
        request.headers['User-Agent'] = header_config['headers']['User-Agent']
        request.headers['Host'] = header_config['headers']['Host']
        request.headers['Origin'] = header_config['headers']['Origin']
        request.headers['Referer'] = header_config['headers']['Referer']
        request.cookies = header_config['cookies']
        print(request)
