# -*- coding: utf-8 -*-
"""
@Time ：2020-02-04 17:12
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

from lxml import etree

# 限制节点的 class 属性为 item-0

html = etree.parse('./1-test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)


