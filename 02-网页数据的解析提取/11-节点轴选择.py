# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-14 14:46
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：XPath 提供了很多节点轴的选择，包括获取子元素，兄弟元素，父元素，祖先元素等
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

# 调用ancestor轴，可以获取所有祖先节点，其后跟两个冒号::，然后是节点选择器，这里直接使用*，表示匹配所有节点
result = html.xpath('//li[1]/ancestor::*')
print(result)
# 在冒号::后面加div，于是结果就只有div这个祖先节点
result = html.xpath('//li[1]/ancestor::div')
print(result)
# 调用attribute轴，可以获取所有属性值，其后跟选择器还是*，代表获取节点的所有属性，返回值是li节点的所有属性值
result = html.xpath('//li[1]/attribute::*')
print(result)
# 调用child轴，可以获取所有直接子节点，这里加了限定条件，选取href属性为link1.html的a节点
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
# 调用descendant轴，可以获取所有子孙节点，这里加限定条件，获取所有span节点，所以返回结果只包含span节点，不包含a节点
result = html.xpath('//li[1]/descendant::span')
print(result)
# 调用following轴，获取当前节点之后的所有节点，虽然使用了*匹配，但又加了索引选择，所以只获取了第二个后续节点
result = html.xpath('//li[1]/following::*[2]')
print(result)
# 调用following-sibling轴，获取当前节点之后的所有同级节点，这里选择使用*匹配，所以获取了所有的后续同级节点
result = html.xpath('//li[1]/following-sibling::*')
print(result)
