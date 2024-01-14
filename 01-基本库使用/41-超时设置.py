# -*- coding: utf-8 -*-
"""
@Time ：2023-04-05 23:18
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：
"""
import requests

# 设置超时时间为 2秒
response = requests.get("https://www.httpbin.org/get", timeout=2)
print(response.status_code)
