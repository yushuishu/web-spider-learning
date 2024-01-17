# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-17 8:30
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

a = doc('.item-0.active a')
print(a)
# 调用text()方法，就可以获取内部的文本信息，此时text()方法会忽略节点内部包含的所有HTML，只返回纯文本内容
print(a.text())
# 要想获取节点内部的HTML，就需要使用html()方法
print(a.html())

print("----------------------------------------------------------------------------------------- 多节点内容获取")
#
lis = doc('li')
print("先打印输出每个节点")
for li in lis.items():
    print(li)
# 分别使用html()方法和text()获取文本内容
# html()方法返回了第一个li节点内部的HTML文本，而text()返回了所有li节点内部的纯文本，各个节点内容中间用一个空格分割开，即返回一个字符串
print(lis.html())
print(lis.text())



