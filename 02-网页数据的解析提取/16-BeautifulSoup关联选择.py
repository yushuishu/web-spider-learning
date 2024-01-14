# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-14 16:14
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：在做选择时，有时不能一步就选到想要的节点，需要先选中某一个节点，再以它为基准选子节点、父节点、兄弟节点
"""

from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')

# 选择子节点和子孙节点，选取节点之后，如果想要获取它的直接子节点，可以调用contents属性，contents得到的结果是直接子节点组成的列表
print(soup.p.contents)
print("------------------------------------------------------------------")
print(soup.p.children)
print("------------------------------------------------------------------")
for i, child in enumerate(soup.p.children):
    print(i, child)
# 如果得到所有子孙节点，则可以调用descendants属性
print("------------------------------------------------------------------")
print(soup.p.descendants)
print("------------------------------------------------------------------")
for i, child in enumerate(soup.p.descendants):
    print(i, child)


# 父节点和祖先节点，这里选择的是第一个a节点的父节点元素，很明显，a节点的父节点时p节点，所以输出结果便是p节点及其内容
# 这里输出的仅仅是a节点的直接父节点，没有再向外寻找父节点的祖先节点，如果想获取所有祖先节点，可以调用parents()
print("------------------------------------------------------------------ 父节点和祖先节点")
html2 = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
        <p class="story">...</p>
"""
soup2 = BeautifulSoup(html2, 'lxml')
print(soup2.a.parent)
print("祖先节点")
print(type(soup2.a.parents))
print(list(enumerate(soup2.a.parents)))


# 兄弟节点
print("------------------------------------------------------------------ 兄弟节点")
html3 = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""
soup3 = BeautifulSoup(html3, 'lxml')
# next_sibling 和 previous_sibling 分别用于获取节点的下一个和上一个兄弟节点，
# next_siblings 和 previous_siblings 分别返回后面和前面的所有兄弟节点
print('Next Sibling', soup3.a.next_sibling)
print('Prev Sibling', soup3.a.previous_sibling)
print('Next Siblings', list(enumerate(soup3.a.next_siblings)))
print('Prev Siblings', list(enumerate(soup3.a.previous_siblings)))


# 提取信息
print("------------------------------------------------------------------ 提取信息")
html4 = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Bob</a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        </p>
"""
soup4 = BeautifulSoup(html, 'lxml')
print('Next Sibling:')
print(type(soup4.a.next_sibling))
print(soup4.a.next_sibling)
print(soup4.a.next_sibling.string)
print('Parent:')
print(type(soup4.a.parents))
print(list(soup4.a.parents)[0])
print(list(soup4.a.parents)[0].attrs['class'])

