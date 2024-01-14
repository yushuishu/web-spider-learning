# -*- coding: utf-8 -*-
"""
@Time ：2020-01-05 11:16
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：
"""

import urllib.request

request = urllib.request.Request('http://httpbin.org/post')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

# Request可以通过参数来构造
# url必传参数
# 如果传data参数，就必须传bytes类型的，如果是字典，可以先用urllib.parse模块的urlencode()编码
# headers是一个字典，构造请求时通过headers参数直接构造，也可以调用请求实列 add_header()方法添加
# 添加请求最常用的用法是修改 User-Agent 来伪装浏览器，默认是Python-urllib

# origin_req_host指定host名或者ip地址
# unverifiable请求是否 是无法验证的。默认false 用户没有权限选择接收这个请求的结果
url = 'https://httpbin.org/post'
urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)


