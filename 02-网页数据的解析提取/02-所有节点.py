# -*- coding: utf-8 -*-
"""
@Time ：2020-02-04 16:39
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

from lxml import etree

# 一般使用 // 开头的 XPath 规则；来选取所有符合要求的节点都会被录取、返回形式是一个列表
# * 代表匹配所有节点、也可以指定节点名称

html = etree.parse('./01-test.html', etree.HTMLParser())
result = html.xpath('//*')
result2 = html.xpath('//li')
print(result)
print(result2)




