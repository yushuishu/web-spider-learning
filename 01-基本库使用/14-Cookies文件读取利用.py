# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/1/9 16:31
# -------------------------------

import http.cookiejar
import urllib.request

# 首先生成 LWP 格式文件
# load()方法读取本地Cookies文件
# 构建 handler 和 Opener

cookie = http.cookiejar.LWPCookieJar()
cookie.load('13-cookies.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))


