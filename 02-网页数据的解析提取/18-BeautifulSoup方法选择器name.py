# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-14 20:30
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：
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
print("-------------------------------------------------------- url")
print(soup.find_all(name='ul'))
print("-------------------------------------------------------- url[0]")
print(type(soup.find_all(name='ul')[0]))

print("-------------------------------------------------------- li")
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))

print("--------------------------------------------------------")
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)

