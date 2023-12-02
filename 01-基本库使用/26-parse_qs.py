# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/1/15 8:56
# -------------------------------

"""
parse_qs(): 反序列化，可以将一串 GET 请求参数转化为 字典
"""

from urllib.parse import parse_qs

query = 'name=germey&age=22'
print(parse_qs(query))



