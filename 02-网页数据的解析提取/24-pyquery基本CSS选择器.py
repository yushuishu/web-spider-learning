# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-15 21:24
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：
"""

from pyquery import PyQuery as pq

html = """
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
"""

doc = pq(html)
print(type(doc('#container .list li')))
print(doc('#container .list li'))
print("----------------------------------------------")
for item in doc('#container .list li').items():
    print("----", item.text())

