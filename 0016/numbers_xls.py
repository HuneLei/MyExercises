# encoding:utf-8
# 使用pandas进行转换
import pandas as pd

txt_path = 'numbers.txt'
excel_path = 'numbers.xls'

with open(txt_path) as f:
    s = eval(f.read(), {})

s = pd.DataFrame(s)
s.to_excel(excel_path, 'numbers', header=False, index=False)
