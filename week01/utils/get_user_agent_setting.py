# ****************************
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 21:12
# Author = kissene_xie
# @File    : get_user_agent_setting
# ****************************
__author__ = 'kissene_xie'

from fake_useragent import UserAgent
ua = UserAgent()

def get_setting():
    config = {}
    headers = {
        "User-Agent": ua.random,
        'Content-Type': 'text/plain; charset=UTF-8',
        "Host": "maoyan.com",
        "Origin": "https://maoyan.com",
        "Referer": "https://maoyan.com/board/4",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
    }
    cookies = r'_lxsdk_cuid=172d168b465c8-07694b0d6af31b-f7d123e-144000-172d168b466c8; _lxsdk=32FE24C0B2E611EA8A833903D31672838A2F645D21064B67B77010041BC9A3BF; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592651238; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1592651238; __mta=150257545.1592651244500.1592651244500.1592651244500.1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=172d168b46f-ae0-993-411%7C%7C12; __mta=150257545.1592651244500.1592651244500.1592651283319.2'
    cookies_dict = {}  # 初始化cookies字典变量
    for line in cookies.split(';'):  # 按照字符：进行划分读取
        # 其设置为1就会把字符串拆分成2份
        name, value = line.strip().split('=', 1)
        cookies_dict[name] = value

    config['headers'] = headers
    config['cookies'] = cookies_dict
    return config


if __name__ == '__main__':
    a = get_setting()
    print(a['headers'])
