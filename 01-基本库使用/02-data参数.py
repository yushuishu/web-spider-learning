# -*- coding: utf-8 -*-
"""
@Time ：2020-01-05 09:57
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({'name': 'lisi'}), encoding='utf-8')
response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
print(response.read().decode('utf-8'))



