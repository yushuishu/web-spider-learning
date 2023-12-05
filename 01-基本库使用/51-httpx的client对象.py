# -*- coding: utf-8 -*-
"""
@Time  ：2023-12-05 22:32
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：httpx 中的 client对象，可以和 requests 中的 session 对象做类比
"""

import httpx

headers = {'User-Agent': 'my-app/0.0.1'}

# 用法1
with httpx.Client(headers=headers) as client:
    response = client.get("https://www.httpbin.org/get")
    print(response.http_version)
    print(response.text)

print("====================================================================")

# 用法2 （等于用法1）
client2 = httpx.Client(headers=headers)
try:
    response2 = client2.get("https://www.httpbin.org/get")
    print(response.http_version)
    print(response2.text)
finally:
    client2.close()
