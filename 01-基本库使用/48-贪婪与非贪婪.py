# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/2/1 11:04
# -------------------------------

import re

print('===========贪婪匹配===========')
# 贪婪匹配
# .* 会匹配尽可能多的字符、正则表达式中 .* 后面的 \d+ 、也就是至少一个数字、并没有指定多少数字
# 结果就会留给 \d+ 一个数字 7
'''
<_sre.SRE_Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
7
'''

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))


print('==========非贪婪匹配==========')
# 非贪婪匹配
# 将第一个 .* 改为 .*?  就转换为非贪婪匹配
# .*? 匹配到 Hello 后面的空白字符时、再向后匹配的就是数字、而 \d+ 恰好可以匹配  .*? 就会停止匹配
'''
<_sre.SRE_Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
1234567
'''

content2 = 'Hello 1234567 World_This is a Regex Demo'
result2 = re.match('^He.*?(\d+).*Demo$', content2)
print(result2)
print(result2.group(1))


print('============注意使用==========')
# 注意使用
# 如果匹配的结果在字符串结尾、 .*? 就有可能匹配不到任何内容
'''
result3 =  
result4 =  kEraCN
'''

context3 = 'http://weibo.com/comment/kEraCN'
result3 = re.match('http.*?comment/(.*?)', context3)
result4 = re.match('http.*?comment/(.*)', context3)
print('result3 = ', result3.group(1))
print('result4 = ', result4.group(1))


