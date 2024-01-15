# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-15 21:39
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：可以用parent()方法获取某个节点的父节点
"""

from pyquery import PyQuery as pq

html = """
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
</div>
"""

doc = pq(html)

# parent()不会继续查找父节点的父节点，即祖先节点
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

print("--------------------------------------------------------------------------")
# 返回所有父节点 以及祖先节点
parents = items.parents()
print(type(parents))
print(parents)

print("--------------------------------------------------------------------------")
# 如果想要筛选祖先节点，可以传入css选择器
parent = items.parents('.wrap')
print(parent)
