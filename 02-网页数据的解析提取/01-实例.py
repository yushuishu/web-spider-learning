# -*- coding: utf-8 -*-
"""
@Time ：2020-02-04 16:17
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

from lxml import etree

# 声明一段HTML文本、调用HTML类进行初始化、构造一个XPath解析对象
# HTML文本的最后一个节点li是没有闭合的、但是etree模块可以自动修正HTML文本
# 调用tostring()方法即可输出修正后的HTML代码、结果是bytes类型、decode()转换str

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
result = etree.tostring(html)
print(result.decode('utf-8'))


print('====================================================================')
# 也可以直接读取文本文件进行解析
html1 = etree.parse('./01-test.html', etree.HTMLParser())
result1 = etree.tostring(html1)
print(result1.decode('utf-8'))





