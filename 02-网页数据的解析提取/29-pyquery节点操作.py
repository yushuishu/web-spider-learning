# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-21 9:56
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

print('------------------------------------------------------------------------------------- removeClass addClass')
# 三次输出，第二次输出时，li节点的active已经在class中不见了，第三次这个class又有了
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)

print('-------------------------------------------------------------------------------------- attr text html')
li.attr('name', 'link')
print(li)
li.text('change item')
print(li)
li.html('<span>changed item</span>')
print(li)

print('-------------------------------------------------------------------------------------- remove')
html2 = """
<div class='wrap'>
    Hello World
    <p>this is paragraph</p>
</div>
"""

doc2 = pq(html2)

wrap = doc2('.wrap')
print(wrap.text())
print('-------------------')
# 想提取Hello World，但是不想要<p>标签内的文本
wrap.find('p').remove()
print(wrap.text())


