# ****************************
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 20:49
# Author = kissene_xie
# @File    : crawling_maoyan
# ****************************
__author__ = 'kissene_xie'

import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import pandas as pd

ua = UserAgent()

mao_yan_url = 'https://maoyan.com/films?showType=3'

def get_moves_info(url, num=10):
    # 初始化数组
    move_list = []
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

    response = requests.get(url, headers=headers, cookies = cookies_dict)
    bs_info = bs(response.text, 'html.parser')
    infos_list = bs_info.find_all('div', attrs={'class': 'movie-hover-info'})
    for infos in infos_list[0:num]:
        move_name = ''
        move_type = ''
        for tags in infos.find_all('div', attrs={'class': 'movie-hover-title'}):
            move_name = tags.get('title')
            tmp = tags.find('span', attrs={'class': 'hover-tag'})
            if tmp is not None:
                if tmp.text == '类型:':
                    move_type = tags.text.split(':')[1].strip()
        move_time = infos.find('div', attrs={'class': 'movie-hover-title movie-hover-brief'}).text.split(':')[1].strip()
        move_list.append([move_name, move_type, move_time])
    # print(move_list)

    if len(move_list) > 0:
        # 使用pandas 整理数据到文件
        movie = pd.DataFrame(data=move_list[:10])
        # windows需要使用gbk字符集
        movie.to_csv('./maoyan.csv', encoding='UTF-8', index=False, header=['影片名称', '类型', '上映日期'])
    else:
        print("数组为空，不生成文件")


if __name__ == '__main__':
    get_moves_info(mao_yan_url)
