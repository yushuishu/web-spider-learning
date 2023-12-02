# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/2/1 15:41
# -------------------------------

import re

'''
在字符串中加入换行符、正则表达式是一样的、用来匹配其中的数字,会报错
这是因为 . 匹配的是除换行符之外的任意字符
使用修饰符 re.S 即可修正错误
re.S 在网页匹配中经常用到、在 HTML 中、节点经常有换行
'''

content = 'Hello 1234567 World_This ' \
          'is a Regex Demo'

reslut = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(reslut.group(1))




