# -*- coding: utf-8 -*-
"""
@Time ：2020-02-01 10:50
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：
"""

import re

# 使用 .* 可以匹配任意字符
# . 可以匹配任意字符、除换行符
# * 代表匹配前面的字符无限次

'''
<_sre.SRE_Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
Hello 123 4567 World_This is a Regex Demo
(0, 41)
'''

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())



