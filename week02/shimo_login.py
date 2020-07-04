# ****************************
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 9:12
# Author = kissene_xie
# @File    : shimo_login
# ****************************
__author__ = 'kissene_xie'

import requests
from fake_useragent import UserAgent
ua = UserAgent(verify_ssl=False)


def login(header, data):
    login_url = "https://shimo.im/lizard-api/auth/password/login"
    s = requests.session()
    # 登录结果
    response = s.post(login_url, data=data, headers=header)
    print('Login Status Code: %s' % response.status_code)
    print('='*40)

    response = s.get('https://shimo.im/dashboard', headers=header)
    print('Dashboard Status Code: %s' % response.status_code)
    print('Body: %s' % response.text)


if __name__ == '__main__':
    headers = {
        "User-Agent": ua.random,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        "Origin": "https://shimo.im",
        "Referer": "https://shimo.im/login?from=home",
        "x-requested-with": "XmlHttpRequest"
    }

    # 登录信息
    postData = {
        'email': 'kissene_xie@163.com',
        'mobile': '+86undefined',
        'password': '1234567890'
    }
    login(headers, postData)
