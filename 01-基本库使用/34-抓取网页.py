# -*- coding: utf-8 -*-
"""
@Time ：2020-01-15 17:15
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：
"""

import requests
import re

# 添加请求头
# 从浏览器请求头中复制，粘贴过来使用
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
r = requests.get('https://ssr1.scrape.center/', headers=headers)
# 使用基本的正则表达式匹配所有标题内容
pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
titles = re.findall(pattern, r.text)
print(titles)



