# encoding:utf-8
# 使用pandas进行转换
import pandas as pd

txt_path = 'city.txt'
excel_path = 'city.xls'

with open(txt_path) as f:
    s = eval(f.read(), {})
    for k, v in s.items():
        if isinstance(v, basestring):
            s[k] = str(v).decode('utf-8')  # 把dict中所有的字符串转成'utf-8'编码

s = pd.DataFrame(s, index=[0]).T
s.to_excel(excel_path, 'city', header=False)
