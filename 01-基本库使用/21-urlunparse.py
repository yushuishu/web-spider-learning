# -*- coding: utf-8 -*-
"""
@Time ：2020-01-14 13:13
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

"""
urlunparse(): 有了urlparse()，相应的就有了它的对立方法 urlunparse()。
            它接收的参数是一个可迭代对象，但是它的长度必须是6，
            否则会抛出参数数量不足或者过多的问题
这里参数data使用列表类型，也可以使用其他类型，比如元组或者特定的数据结构
"""

from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))


