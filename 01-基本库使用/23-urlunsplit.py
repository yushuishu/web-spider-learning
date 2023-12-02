# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/1/14 13:41
# -------------------------------

"""
urlunsplit(): 与 urlunparse() 方法类型，也是将链接各个部分组合成完整链接的方法
            传入的参数也是可迭代对象，比如 列表、元组，唯一区别是长度必须为5
"""

from urllib.parse import urlunsplit

data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))



