# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-14 15:07
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：Beautiful Soup 是 Python 的一个 HTML或xml的解析库
    由以下表格看出，LXML解析器有解析HTML和XML的功能，而且速度快，容错能力强，所以推荐使用它。需要安装 Beautiful Soup 和 lxml 这两个库。
    pip3 install beautifulsoup4
"""

"""
| 解析器 | 使用方法 | 优势 |劣势 |
| :-- | :-- | :-- |:-- |
| Python标准库 | BeautifulSoup(markup, 'html.parser') | Python的内置标准库，执行速度适中，文档容错能力强 | Python2.7.3 或 3.2.2前的版本中文容错能力差，需要C语言库 |
| LXML HTML解析器  | BeautifulSoup(markup, 'lxml') | 速度快，文档容错能力强 | 需要安装C语言库 |
| LXML XML解析器 | BeautifulSoup(markup, 'xml') | 速度快，唯一支持xml的解析器 | 需要安装C语言库 |
| html5lib | BeautifulSoup(markup, 'html5lib') | 提供最好的容错性，以浏览器的方式解析文档，生成HTML5格式文档 | 速度慢，不依赖外部扩展 |
"""