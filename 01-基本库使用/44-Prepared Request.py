# -*- coding: utf-8 -*-
"""
@Time ：2020-01-31 15:21
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

from requests import Request, Session

# urllib 中可以将请求表示为数据结构、其中各个参数可以通过一个request对象来表示
# 在 requests 中同样可以做到，这个数据结构就叫 Prepared Request

# 引入 Request 、然后用 url data headers 参数构造了一个 Request 对象
# 这时再调用Session的prepare_request() 方法将其转换为一个 Prepared Request 对象
# 然后调用 send() 方法发送

url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)



