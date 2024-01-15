# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-15 21:30
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：查询子节点，需要用到find() 方法，其参数是css选择器
"""

from pyquery import PyQuery as pq

html = """
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
"""

doc = pq(html)
items = doc(".list")
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)

print("------------------------------------------------------------------------------")

# find()方法是查找范围是节点的所有子孙节点，如果只想查找子节点，那么可以用children()方法
lis = items.children()
print(type(lis))
print(lis)

print("------------------------------------------------------------------------------")

# 要筛选所有子节点中，符合条件的节点，列如想筛选出子节点中class为active的节点
lis = items.children('.active')
print(type(lis))
print(lis)

