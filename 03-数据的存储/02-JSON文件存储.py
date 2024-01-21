# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-21 11:56
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：
"""

import json

# json数据需要使用双引号，不可以使用单引号
jsonStr = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "旺财",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''

print(type(jsonStr))
data = json.loads(jsonStr)
print(data)
print(type(data))
# 获取元素
print(data[0]['name'])
print(data[0].get('name'))

print('------------------------------------------------- json数据写入文件')
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(jsonStr)

print('------------------------------------------------- 从文件读取json')
with open('data.json', 'r', encoding='utf-8') as file:
    strData = file.read()
    data = json.loads(strData)
    print(data)
