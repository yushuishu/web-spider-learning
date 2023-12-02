# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/1/5 16:55
# -------------------------------

import http.cookiejar
import urllib.request

filename = '12-cookies.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)


