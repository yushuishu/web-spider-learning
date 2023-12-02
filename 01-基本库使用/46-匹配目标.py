# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/2/1 10:39
# -------------------------------

import re

# 从字符串中提取一部分内容
# 使用 () 可以将想提取的子字符串括起来
# 想提取数字、可以将数字部分的正则表达式用括号 () 括起来、然后调用 group(1) 获取匹配结果
# 如果后面还有括号、依次是 group(2)、group(3)

'''
<_sre.SRE_Match object; span=(0, 19), match='Hello 1234567 World'>
Hello 1234567 World
1234567
(0, 19)
'''

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())




