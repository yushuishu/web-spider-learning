# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-21 10:42
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：
"""

import requests
from pyquery import PyQuery as pq
import re

url = 'https://ssr1.scrape.center/'
html = requests.get(url).text
doc = pq(html)
items = doc('.el-card').items()

'''
打开方式：
    r: 以只读方式打开，默认模式
    rb: 以二进制只读打开，通常用于打开二进制文件，列如 音频、图片、视频
    r+: 以读写方式打开，即可以读文件，又可以写文件
    rb+: 以二进制读写打开，同样即可以读文件，又可以写文件，只不过读取和写入都是二进制数据
    w: 以写入方式打开文件。如果该文件已经存在，则将覆盖；如果文件不存在，则创建新文件
    wb: 以二进制写入方式打开文件。如果该文件已经存在，则将覆盖；如果文件不存在，则创建新文件
    w+: 以读写方式打开。如果该文件已经存在，则将覆盖；如果文件不存在，则创建新文件
    wb+: 以二进制读写格式打开。如果该文件已经存在，则将覆盖；如果文件不存在，则创建新文件
    a: 以追加方式打开文件.如果该文件已经存在，则文件指针将会放在文件的结尾，新内容将会写到已知内容后面，如果文件不存在，则创建新文件
    a+: 以读写方式打开文件.如果该文件已经存在，则文件指针将会放在文件的结尾，新内容将会写到已知内容后面，如果文件不存在，则创建新文件
    ab+: 以二进制追加方式打开一个文件，如果该文件已存在，则文件指针将会放在文件结尾，如果文件不存在，则创建新文件
'''
with open('movies.txt', 'w', encoding='utf-8') as file:
    for item in items:
        print(item)
        # 名称
        name = item.find('a > h2').text()
        file.write(f'名称: {name}\n')
        # 类别
        categories = [item.text() for item in item.find('.categories button span').items()]
        file.write(f'类别: {categories}\n')
        # 上映时间
        published_at = item.find('.info:contains(上映)').text()
        published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
            if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None
        file.write(f'上映时间: {published_at}\n')
        # 评分
        score = item.find('p.score').text()
        file.write(f'评分: {score}\n')
        file.write(f'{"=" * 50}\n')
