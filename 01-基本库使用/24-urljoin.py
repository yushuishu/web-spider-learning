# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/1/14 13:48
# -------------------------------

"""
urljoin(): 提供了一个base_url (基础链接) 作为第一个参数，将新的链接作为第二个参数
        该方法会分析base_url 的 scheme、netloc、path 这3个内容，并对新链接缺失的部分
        进行补充，返回结果

运行结果：
        https://www.baidu.com/FAQ.html
        https://cuiqingcai.com/FAQ.html
        https://cuiqingcai.com/FAQ.html
        https://cuiqingcai.com/FAQ.html?question=2
        https://cuiqingcai.com/index.php
        https://www.baidu.com?category=2#comment
        www.baidu.com?category=2#comment
        www.baidu.com?category=2
base_url 提供了三项内容，如果这3项在新的链接里不存在，就给予补充、
如果新链接存在，就使用新的链接的部分，而 base_url 中的 scheme、netloc、path 是不起作用的
通过 urljoin() 方法，就可以实现链接的解析、拼合与生成
"""

from urllib.parse import urljoin

print(urljoin('https://www.baidu.com', 'FAQ.html'))
print(urljoin('https://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('https://www.baidu.com/about,html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('https://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('https://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))



