# -*- coding: utf-8 -*-
"""
@Time ：2020-01-05 10:17
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：
"""

import urllib.request
import urllib.error
import socket

# 设置超时时间是0.1秒 未响应时 跳过它的抓取

try:
    response = urllib.request.urlopen('https://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('time out')

