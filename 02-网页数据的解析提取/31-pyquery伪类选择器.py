# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-21 10:10
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

li = doc('li:first-child')
print(li)
print('---------------------------- last-child 最后一个节点')
li = doc('li:last-child')
print(li)
print('---------------------------- nth-child(2) 奇偶数节点')
li = doc('li:nth-child(2)')
print(li)
print('---------------------------- gt(2) 奇偶数节点')
li = doc('li:gt(2)')
print(li)
print('---------------------------- nth-child(2n) 奇偶数节点')
li = doc('li:nth-child(2n)')
print(li)
print('---------------------------- contains(second) 包含某一文本的节点')
li = doc('li:contains(second)')
print(li)

