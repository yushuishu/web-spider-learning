# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-17 8:14
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：
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

print("----------------------------------------------------------------------------- 单个节点")
li = doc('.item-0.active')
# 如果节点是单个节点，可以直接打印输出，也可以直接转成字符串
print(li)
print(str(li))

print("----------------------------------------------------------------------------- 遍历多个节点")

# 结果是多个节点，需要遍历获取，需要调用items()方法

lis = doc('li').items()
print(type(lis))
for li in lis:
    print(type(li), li)

print("------------------------------------------------------------------------------- 获取属性")

a = doc('.item-0.active a')
print(type(a), a)
print(a.attr('href'))
# 多个元素
a = doc('a')
print(type(a), a)
print(a.attr('href'))
print(a.attr.href)
# 选中的节点打印有4个，调用attr()方法，返回的结果只有一个，如果获取所有a节点的元素，就需要通过遍历获取
print("------------------")
for item in a.items():
    print(item.attr('href'))
