# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/1/15 9:10
# -------------------------------

"""
unquote(): 可以将使用 quote() 方法对 URL 编码后的结果进行还原
运行结果: https://www.baidu.com/s?wd=壁纸
"""

from urllib.parse import unquote

url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))


