# -*- coding: utf-8 -*-
"""
@Time ：2020-01-05 10:04
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import urllib.request

# timeout参数用于超时时间 单位：秒
# 超时会抛出异常 During handling of the above exception, another exception occurred:
# 该异常属于 urllib.error 模块
# 支持：http HTTPS ftp 请求

response = urllib.request.urlopen('https://httpbin.org/get', timeout=0.1)
print(response.read())

