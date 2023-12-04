# -*- coding: utf-8 -*-
"""
@Time ：2020-01-15 08:56
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

"""
parse_qs(): 反序列化，可以将一串 GET 请求参数转化为 字典
"""

from urllib.parse import parse_qs

query = 'name=germey&age=22'
print(parse_qs(query))



