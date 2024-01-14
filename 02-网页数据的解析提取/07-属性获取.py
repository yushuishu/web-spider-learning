# -*- coding: utf-8 -*-
"""
@Time ：2020-02-05 10:23
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：
"""

from lxml import etree

# 通过 @href 即可获取节点的 href 属性、此处和属性匹配的方法不同、属性匹配是中括号加属性名和值
# 来限定某个属性、如 [@href="link1.html"] 、此处的 @href 指的是获取节点的某个属性

html = etree.parse('./01-test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)



