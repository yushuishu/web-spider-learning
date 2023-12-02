# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/1/15 16:43
# -------------------------------

"""
requests:
urllib 库中的 urlopen() 方法实际上是以 GET 方式请求，而 requests 中相应的方法就是 get 方法

调用 get() 方法实现与 urlopen() 相同的操作，得到一个 Response 对象
输出 Response 类型、状态码、响应体类型、内容、Cookies
返回的类型是 str 类型，但是它很特殊，是 JSON 格式的。如果想直接解析返回的结果，得到一个字典
格式的话，可以直接调用 json() 方法

requests 中的请求都可以用一句话完成：
            r = requests.post('https://httpbin.org/post')
            r = requests.put('https://httpbin.org/put')
            r = requests.delete('https://httpbin.org/delete')
            r = requests.head('https://httpbin.org/get')
            r = requests.options('https://httpbin.org/get')
"""

import requests

r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

print("=================================================================================")
r2 = requests.get('https://www.httpbin.org/get')
print(type(r2))
print(r2.status_code)
print(type(r2.text))
print(r2.text)
print(r2.cookies)




