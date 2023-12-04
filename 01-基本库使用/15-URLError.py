# -*- coding: utf-8 -*-
"""
@Time ：2020-01-09 17:23
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''

urllib的 error 模块定义了由 request 模块产生的异常。
如果出现问题，request 模块便会抛出 error 模块中定义的异常

'''

# URLError
# URLError 来自 urllib 库的 error 模块，继承自 OSError 类，是 error 异常模块的基类
# request 模块产生的异常 都可以通过捕获这个类来处理

# 打开一个不存在的页面，不会报错，运行结果是 Not Found

from urllib import request, error
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)


