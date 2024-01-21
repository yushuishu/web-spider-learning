# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-21 10:17
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：parsel库可以解析HTML 和 xml，并支持使用xpath 和 css 选择器对内容进行提取和修改，同时还融合了正则表达式的提取功能，
        同时也是 python最流行的爬虫框架Scrapy的底层支持
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

# 输出类型都是 <class 'parsel.selector.SelectorList'> ，这是一个可迭代对象。
# css 选择器给于首先被转成xpath，真正用于节点提取的事xpath
selector = Selector(text=html)
items = selector.css('.item-0')
print(len(items), type(items), items)
items2 = selector.xpath('//li[contains(@class, "item-0")]')
print(len(items2), type(items), items2)

