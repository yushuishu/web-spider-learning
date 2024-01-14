# -*- coding: utf-8 -*-
"""
@Time ：2020-01-15 09:00
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：
"""

"""
parse_qsl(): 可以将参数转化为元组组成的列表
"""

from urllib.parse import parse_qsl

query = 'name=germey&age=22'
print(parse_qsl(query))



