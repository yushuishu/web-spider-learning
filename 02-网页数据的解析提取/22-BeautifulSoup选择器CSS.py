# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-14 20:52
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：使用CSS选择器，只需要调用select()方法，传入相应的CSS选择器即可
"""

from bs4 import BeautifulSoup

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''


soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))

print("---------------------------------------------------- 嵌套选择")
soup2 = BeautifulSoup(html, 'lxml')
for ul in soup2.select('ul'):
    print(ul.select('li'))

print("---------------------------------------------------- 获取属性")
soup3 = BeautifulSoup(html, 'lxml')
for ul in soup3.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

print("---------------------------------------------------- 获取文本")
soup4 = BeautifulSoup(html, 'lxml')
for li in soup4.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)

