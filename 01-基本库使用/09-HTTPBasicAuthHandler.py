# -*- coding: utf-8 -*-
"""
@Time ：2020-01-05 16:02
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：
"""


from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

# CRM项目
# 问题：网站打开时弹出提示框，需要输入用户名和密码，验证成功后，才可以查看页面
# 解决：HTTPBasicAuthHandler

# 首先实列化 HTTPBasicAuthHandler 对象，参数是 HTTPPasswordMgrWithDefaultRealm 对象，利用
# add_password() 添加进去用户名和密码，就会建立一个验证的 Handler
# 利用 Handler 并使用 build_opener() 方法构建一个 Opener ，Opener在发送请求时，就相当验证成功
# 利用 Opener 的 open() 方法打开链接，就可以完成验证。结果就是验证后的页面源码内容
username = 'username'
password = 'password'
url = 'http://localhost:8080/A1-ZYCRMTEST/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)


