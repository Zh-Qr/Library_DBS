"""
作者：仲启瑞
联系方式：
TEL:18305125976
QQ：1062127784
"""
import pandas as pd

# 读取 Excel 文件
file_path = 'test.xlsx'
df = pd.read_excel(file_path)

data = df.values
# 显示读取的数据
# print(data)

for row in data:
    print(row)