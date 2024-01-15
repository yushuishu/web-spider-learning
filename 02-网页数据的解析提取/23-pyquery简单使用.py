# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-15 21:06
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：使用pyquery，需要先初始化一个PyQuery对象。初始化的方式有很多种，：字符串、传入URL、传入文件名等
"""
import requests
from pyquery import PyQuery as pq

html = """
<div>
    <ul>
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
"""

doc = pq(html)
print(doc('li'))

print("-------------------------------------------------------------------------------")

# PyQuery会先请求这个url，得到HTML内容完成初始化
doc2 = pq(url="https://cuiqingcai.com")
#doc2 = pq(requests.get('https://cuiqingcai.com').text)
print(doc2('title'))

print("-------------------------------------------------------------------------------")
doc3 = pq(filename="01-test.html")
print(doc3('li'))
