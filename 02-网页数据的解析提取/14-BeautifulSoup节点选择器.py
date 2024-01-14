# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-14 15:54
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：直接调用节点的名称即可选择节点，然后调用string属性就可以得到节点内的文本，这种选择方式速度非常快，
    当单个节点结构层次清晰时，可以选择这种方式解析
"""

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
print(soup.title)
# bs4.element.Tag 是BeautifulSoup中的一个重要的市规划局结构，经过选择器选择的结果都是这种Tag类型，Tag类型具有一些属性，如：string，
# 调用次属性，就可以得到节点的文本内容
print(type(soup.title))
print(soup.title.string)
print(soup.head)
# 后面p节点并没有选择到，当有多个节点时，这种选择方式只会选择到第一个匹配的节点
print(soup.p)
