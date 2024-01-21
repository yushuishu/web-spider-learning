# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-21 10:27
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：
"""

from parsel import Selector

html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

selector = Selector(text=html)
items = selector.css('.item-0')
for item in items:
    text = item.xpath('.//text()').get()
    print(text)

print('------------------------------ get()只提取第一个对象')
result = selector.xpath('//li[contains(@class, "item-0")]//text()').get()
print(result)

print("------------------------------ getall() 提取所有")
result = selector.css('.item-0 *::text').getall()
print(result)

print("------------------------------ css 实现方式")
result = selector.css('.item-0::text').get()
print(result)

