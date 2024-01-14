# -*- coding: utf-8 -*-
"""
@Time ：2020-01-14 14:27
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：
"""

"""
urlencode(): 构造 GET 请求参数的时候非常有用
首先声明一个字典来将参数表示出来，然后调用 urlencode() 方法将其序列化为 GET 请求参数
"""

from urllib.parse import urlencode

params = {
    'name': 'lisi',
    'age': 22
}
base_url = 'https://www.baidu.com?'
url = base_url + urlencode(params)
print(url)



