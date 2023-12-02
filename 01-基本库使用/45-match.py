# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/1/31 15:46
# -------------------------------

import re

# match 方法中、第一个参数是正则表达式、第二个参数是匹配的字符串
# 打印输出是 SRE_Match 对象、证明匹配成功
# group() 方法可以输出匹配的内容

'''
41
<_sre.SRE_Match object; span=(0, 25), match='Hello 123 4567 World_This'>
Hello 123 4567 World_This
(0, 25)
'''

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())


