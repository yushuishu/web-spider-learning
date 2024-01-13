# -*- coding: utf-8 -*-
"""
@Time ：2020-02-05 11:01
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

from lxml import etree

# 增加一个属性 name 、要确定节点、需要根据 class 和 name 属性来选择、两个条件需要满足、使用 and

text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)


