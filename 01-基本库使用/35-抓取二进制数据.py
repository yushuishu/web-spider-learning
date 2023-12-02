# -------------------------------
# @Author : 谁书-ss
# @Time   : 2020/1/30 14:59
# -------------------------------

import requests

# GitHub
# 抓取站点图标，也就是浏览器标签上显示的图标
# 前两行是 r.text 的结果  最后一行是 r.content 结果、开头的 b 代表 bytes 类型的数据
# 由于图片是二进制数据，所以 r.text 转换字符串时出现乱码

r = requests.get('https://github.com/favicon.ico')
print(r.text)
print("\n")
print(r.content)

# 图片保存
# 使用 open 方法、第一个参数是文件名、第二个参数代表二进制写的形式打开，可以向文件里写入二进制数据集
with open('../01-基本库使用/35-favicon.icon', 'wb') as f:
    f.write(r.content)


