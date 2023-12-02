# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/2/4 16:47
# -------------------------------

from lxml import etree

# 通过追加 /a 即可选择所有 li 节点的所有直接 a 子节点
# 如果选取子孙节点、就可以用 //

html = etree.parse('./1-test.html', etree.HTMLParser())

result = html.xpath('//li/a')
result2 = html.xpath('//ul//a')

print(result)
print(result2)



