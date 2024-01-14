# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-14 15:23
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：声明一个不是完整的HTML 字符串，body节点 和 HTML节点 都没有闭合
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
# prettify()，可以把要解析的字符串以标准格式输出，输出结果包含了body节点 和 HTML节点，
# 也就是说BeautifulSoup会自动更正格式。注意字符串是在初始化BeautifulSoup时更正的，prettify()方法只是进行缩进处理；
print(soup.prettify())
print("----------------------------------------------------------")
# 输出节点内容
print(soup.title.string)

