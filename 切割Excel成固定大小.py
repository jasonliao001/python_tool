# -*- coding: utf-8 -*-
import pandas as pd
import math
execl_path = f"./商品信息导入模板.xlsx"
df = pd.read_excel(execl_path)
rows, cols = df.shape
split_num = 300
value = math.floor(rows / split_num)
rows_format = value * split_num
new_list = [[i, i + split_num] for i in range(0, rows_format, split_num)]
for i_j in new_list:
    i, j = i_j
    excel_small = df[i:j]
    excel_small.to_excel('./文档A/A_{0}_{1}.xlsx'.format(i, j), index=False)
last = df[rows_format:]
last.to_excel('./文档A/A_last.xlsx', index=False)
