# -*- coding: utf-8 -*-
"""
@Time  ：2024-01-21 14:06
@Auth  ：谁书-ss
@IDE   ：PyCharm
@Motto ：ABC(Always Be Coding)
@Description ：
"""

import csv
import pandas as pd

# 不加参数newline='' 写入的数据，会出现空行
with open('data.csv', 'w', encoding='utf-8', newline='') as file:
    # 默认逗号分隔
    writer = csv.writer(file)
    # 指定分隔符，空格分隔
    #writer = csv.writer(file, delimiter=' ')

    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['101', '张三', 25])
    writer.writerow(['102', '王五', 20])
    writer.writerow(['103', '旺财', 30])
    writer.writerow(['104', '小红', 22])

# 一次性写入多条数据
with open('data2.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'name', 'age'])
    writer.writerows([['101', '张三', 25], ['102', '王五', 20], ['103', '旺财', 30], ['104', '小红', 22]])

print('---------------------------------------------------- 读取数据')

with open('data.csv', 'r', encoding='utf-8') as file:
    rows = csv.reader(file)
    for row in rows:
        print(row)

print('---------------------------------------------------- 读取数据 pandas')
df = pd.read_csv('data.csv')
print(df)
print('pandas 数据转列表或元组：', df.values.tolist())
# 遍历
for index, row in df.iterrows():
    print(f'序号：{index}，数据行：{row.tolist()}')
