# -*- coding: utf-8 -*-
"""
@Time ：2020-01-31 14:41
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import requests

# 使用 proxies 参数

proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080'
}
requests.get('https://taobao.com', proxies=proxies)

# 若代理需要使用 HTTP Basic Auth 可以使用类似 http://user:password@host:port 这样的语法设置代理
proxies2 = {
    'http': 'http://user:password@10.10.1.10:3128',
}
requests.get('https://taobao.com', proxies=proxies2)

# requests 还支持 SOCKS 协议的代理
proxies3 = {
    'http': 'socks5://user:password@host:port',
    'https': 'socks5://user:password@host:port'
}
requests.get('https://taobao.com', proxies=proxies3)
