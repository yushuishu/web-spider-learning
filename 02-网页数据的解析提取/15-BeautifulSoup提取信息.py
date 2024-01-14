# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-14 16:02
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：string属性获取文本的值，如何获取节点名称？
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

# 获取名称
print(soup.title.name)

# 获取属性
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])  # 返回一个字符串，name属性是唯一的
print(soup.p['class']) # 返回一个列表，class属性，一个节点可以包括多个class

# 获取内容，
print(soup.p.string)

# 嵌套选择，tag类型对象可以继续调用节点进行下一步的选择，例如获取head节点，继续调用head选取内部的head节点
html2 = """
<html><head><title>The Dormouse's story</title></head>
<body>
"""
soup2 = BeautifulSoup(html2, 'lxml')
print(soup2.head.title)
print(type(soup2.head.title))
print(soup2.head.title.string)
