# -*- coding: utf-8 -*-
"""
@Time ：2020-01-14 13:21
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

"""
urlsplit(): 和 urlparse() 方法相似，只不过不能单独解析 params 这一部分
            只返回5个结果，params 会合并到 path 中
返回结果 SplitResult: 它其实是一个元组类型，既可以用属性获值，也可以索引获值
"""

from urllib.parse import urlsplit

result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(result)
print(result.scheme, result[0])


