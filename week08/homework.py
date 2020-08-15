# ****************************
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/15 14:28
# Author = kissene_xie
# @File    : homework
# ****************************
__author__ = 'kissene_xie'
import time

# 作业一
# Q1 区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
# list tuple str dict collections.deque
# 可变序列: list, dict
# 不可变序列: str, tuple, collections.deque
# 容器序列: list, tuple, dict
# 扁平序列: str, collections.deque


# 作业二
# 自定义一个 python 函数，实现 map() 函数的功能。
def my_map(func, *iterables):
    res = []
    for args in zip(*iterables):
        res.append(func(*args))
    return res


# 作业三
# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
def timer(func):
    def run_time(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__}运行时间: {end_time - start_time}')
    return run_time


@timer
def test():
    time.sleep(1)


if __name__ == '__main__':
    print(my_map(lambda x: x * 2, [1, 2, 3]))
    test()
