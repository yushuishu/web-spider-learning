# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-14 14:38
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：在选择节点时，可能同时匹配了多个节点，但我们只想要其中某一个节点，如第二个或者最后一个
"""

from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''
html = etree.HTML(text)

# 选取第一个li节点
result = html.xpath('//li[1]/a/text()')
print(result)
# 选取最后一个li节点
result = html.xpath('//li[last()]/a/text()')
print(result)
# 选取位置小于3的li节点
result = html.xpath('//li[position()<3]/a/text()')
print(result)
# 选取最后一个节点减2的节点：last()-2
result = html.xpath('//li[last()-2]/a/text()')
print(result)

