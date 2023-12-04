# -*- coding: utf-8 -*-
"""
@Time ：2020-01-31 10:10
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import requests

# 利用 session 对象维持同一个会话，相当于打开一个新的浏览器选项卡、而不是新的浏览器
# 不用担心cookies问题、通常用于模拟登陆成功之后再进行下一步的操作
# 设置一个 cookie 名称叫作 number 、内容是 123456789、随后又请求 http://httpbin.org/cookies
# 此时的网址可以获取当前的 Cookies

s = requests.session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)



