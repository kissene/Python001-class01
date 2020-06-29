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
import pandas as pd
from week01.utils.get_user_agent_setting import get_setting


mao_yan_url = 'https://maoyan.com/films?showType=3'

def get_moves_info(url, num=10):
    # 初始化数组
    move_list = []
    header_config = get_setting()

    response = requests.get(url, headers=header_config['headers'], cookies=header_config['cookies'])
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
        movie = pd.DataFrame(data=move_list)
        # windows需要使用gbk字符集
        movie.to_csv('./maoyan.csv', encoding='UTF-8', index=False, header=['影片名称', '电影类型', '上映时间'])
    else:
        print("数组为空，不生成文件")


if __name__ == '__main__':
    get_moves_info(mao_yan_url)
