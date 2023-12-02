# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/2/5 10:12
# -------------------------------

from lxml import etree

# 如果想要获取 li 节点内部文本、一种是选取 a 节点再获取文本、另一种就是使用 //

html = etree.parse('./1-test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')
result2 = html.xpath('//li[@class="item-0"]//text()')
print(result)
print(result2)

# 要想获取子孙节点内部的所有文本、就直接使用 // 加 text() 的方式
# 获取特定子孙节点下的文本、就先选取特定的子孙节点、再调用 text() 方法获取

