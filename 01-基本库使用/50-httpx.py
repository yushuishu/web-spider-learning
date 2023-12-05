# -*- coding: utf-8 -*-
"""
@Time ：2023-12-05 22:15
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：urllib 和 requests 已经可以爬取绝大多数网站，但是对于一些强制使用 HTTP/2.0 协议访问的网站，就无法使用，
            httpx 就是一个非常流行的功能强大的第三方库，功能强大。requests支持的功能，httpx都支持，使用方式几乎一样。
            安装方式：pip3 install "httpx[http2]"
            pip3 install httpx 是不支持 http2协议的
"""

import httpx

# httpx.get() 和 requests.get() 使用方式一样，只有在使用httpx请求HTTP/2.0协议时，API是不同的
# 默认是不支持 HTTP/2.0的，是需要开启支持 http2=True
# response = httpx.get("https://spa16.scrape.center")

client = httpx.Client(http2=True)
response = client.get("https://spa16.scrape.center")
print(response.status_code)
# http_version 是 requests 中不存在的方法
print(response.http_version)
print(response.headers)
print(response.text)
