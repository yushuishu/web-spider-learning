# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/2/4 16:39
# -------------------------------

from lxml import etree

# 一般使用 // 开头的 XPath 规则；来选取所有符合要求的节点都会被录取、返回形式是一个列表
# * 代表匹配所有节点、也可以指定节点名称

html = etree.parse('./1-test.html', etree.HTMLParser())
result = html.xpath('//*')
result2 = html.xpath('//li')
print(result)
print(result2)




