# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/1/15 9:00
# -------------------------------

"""
parse_qsl(): 可以将参数转化为元组组成的列表
"""

from urllib.parse import parse_qsl

query = 'name=germey&age=22'
print(parse_qsl(query))



