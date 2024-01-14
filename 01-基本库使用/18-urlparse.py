# -*- coding: utf-8 -*-
"""
@Time ：2020-01-13 12:04
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：
"""

"""

urllib 库提供的 parse 模块，它定义了处理 URL 的标准接口
例如实现 URL 各部分的抽取、合并、链接转换

"""

# 该方法实现 URL 的识别和分段。利用 urlparse() 方法进行解析
# 返回结果是一个 ParseResult 类型的对象
# 它包含六个部分，分别是： scheme、netloc、path、params、query、fragment

# <class 'urllib.parse.ParseResult'> ParseResult(scheme='http', netloc='www.baidu.com',
# path='/index.html', params='user', query='id=5', fragment='comment')

# urlparse() 方法将其拆分6个部分
# ://前面的是 scheme 代表协议、第一个符号 / 前面是 netloc 代表域名、/ 后面是 path、
# 分号 ; 后面是 params 代表参数
# 问号 ? 后面是查询条件 query ，一般用于 GET 类型的URL、 # 号后面是锚点，用于直接定位页面内部的下拉位置

# 标准链接格式：scheme://netloc/path;params?query#fragment

from urllib.parse import urlparse

result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)


