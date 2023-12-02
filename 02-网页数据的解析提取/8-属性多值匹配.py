# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/2/5 10:47
# -------------------------------

from lxml import etree

# 节点有多个值、使用属性匹配获取、就无法匹配、此时就需要使用 contains() 函数
# 第一个参数传入属性名称、第二参数传入属性值

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)



