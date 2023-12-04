# -*- coding: utf-8 -*-
"""
@Time ：2020-01-15 09:10
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""

"""
unquote(): 可以将使用 quote() 方法对 URL 编码后的结果进行还原
运行结果: https://www.baidu.com/s?wd=壁纸
"""

from urllib.parse import unquote

url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))


