# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-21 10:36
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：正则提取
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
# re 匹配所有符合规则的节点
result = selector.css('.item-0').re('link.*')
print(result)
# re_first 提取第一个符合规则的节点
result = selector.css('.item-0').re_first('<span class="bold">(.*?)</span>')
print(result)

