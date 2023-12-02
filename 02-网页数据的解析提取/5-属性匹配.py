# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/2/4 17:12
# -------------------------------

from lxml import etree

# 限制节点的 class 属性为 item-0

html = etree.parse('./1-test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)


