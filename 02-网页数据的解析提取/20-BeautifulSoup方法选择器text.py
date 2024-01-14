# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-14 20:30
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：
"""

from bs4 import BeautifulSoup
import re

html = '''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
# text参数可以用来匹配节点的文本，传入形式可以使字符串，也可以使正则表达式对象
print(soup.find_all(text=re.compile('link')))

