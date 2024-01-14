# -*- coding: utf-8 -*-
"""
@Time ：2023-04-05 23:15
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：
"""

import requests

files = {"files": open("35-favicon.icon", "rb")}
response = requests.post("https://www.httpbin.org/post", files=files)
print(response.text)
