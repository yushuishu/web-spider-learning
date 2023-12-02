# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/1/15 17:00
# -------------------------------

import requests

r = requests.get('https://httpbin.org/get')
print(r.text)
print("=====================================================================")
# 附加额外的信息: 一般信息数据会用字典来存储
# 添加两个参数 name 是 germey ，age 是 22
# 请求的链接自动被构造成：http://httpbin.org/get?age=22&name=germey
data = {
    'name': 'germey',
    'age': 22
}
r2 = requests.get('https://httpbin.org/get', params=data)
print(r2.text)

