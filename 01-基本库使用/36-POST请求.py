# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/1/30 15:25
# -------------------------------

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




