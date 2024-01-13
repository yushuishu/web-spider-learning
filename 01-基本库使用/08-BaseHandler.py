# -*- coding: utf-8 -*-
"""
@Time ：2020-01-05 15:10
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# urllib.request模块里的BaseHandler类，它是所有的其他 Handler 的父类，它提供最基础的方法
# 如：default——open() protocol_request()

# Handler子类继承这个BaseHandler类
# HTTPdefaultErrorHandler: 处理HTTP响应错误， 错误都会抛出 HTTPError类型异常
# HTTPRedirectHandler: 处理重定向
# HTTPCookieProcessor: 处理Cookie
# ProxyHandler: 设置代理，默认代理空
# HTTPPasswordMgr: 管理密码，维护用户名和密码表
# HTTPBasicAuthHandler: 管理认证，解决认证问题

# 参考文档： https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler

