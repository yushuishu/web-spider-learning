# -*- coding: utf-8 -*-
"""
@Time ：2020-01-31 14:56
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import requests
from requests.auth import HTTPBasicAuth

# 如果用户名和密码正确、就会返回200状态码；验证失败，就会返回401状态码
r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
print(r.status_code)

# requests 提供一个更简洁的写法、可以直接传一个元组、它会默认使用 HTTPBasicAuth 这个类来验证
r2 = requests.get('http://localhost:5000', auth=('username', 'password'))
print(r2.status_code)



