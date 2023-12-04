# -*- coding: utf-8 -*-
"""
@Time ：2020-01-30 15:25
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import requests
import time

data = {'name': 'germey', 'age': '22'}
r = requests.post("https://httpbin.org/post", data=data)
print(type(r))
print(type(r.status_code), r.status_code)
print(type(r.text), r.text)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)




