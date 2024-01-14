# -*- coding: utf-8 -*-
"""
@Time ：2020-01-05 09:45
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：
"""

import urllib.request

# urlopen参数：urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, context=None)
# data：需要使用bytes方法将参数转化为字节流编码格式的内容，即 bytes 类型，并且 传递该参数，请求方式也不再是 GET 而是 POST
# [timeout,]*：

response = urllib.request.urlopen('https://www.python.org')

print('================== 响应的类型')
# 得到HTTPResponse类型对象
# 主要包含read()、readinto()、getheader(name)、getheaders()、fileno()等方法
# msg version status reason debuglevel closed等属性
print(type(response))

print('=================== 响应网页源代码')
print(response.read().decode('utf-8'))

print('=================== 状态码 响应头 server')
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

