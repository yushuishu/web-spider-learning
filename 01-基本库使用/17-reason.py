# -*- coding: utf-8 -*-
"""
@Time ：2020-01-12 18:34
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import socket
import urllib.request
import urllib.error

# reason 属性返回的不一定是字符串，也可能是一个对象
# 设置超时时间，强制抛出 timeout 异常
# reason 属性的结果是 socket.timeout 类，可以用isinstance() 方法来判断类型

try:
    response = urllib.request.urlopen('https://baidu,com', timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')



