# -*- coding: utf-8 -*-
"""
@Time ：2020-01-15 09:04
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
@Description ：
"""

"""
quote(): 将内容转化为 URL 编码的格式，URL 中带有中文参数时，有可能导致乱码的问题
        此时该方法可以将中文转化为 URL 编码
运行结果: https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8
"""

from urllib.parse import quote

keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)



