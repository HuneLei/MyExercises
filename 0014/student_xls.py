# encoding:utf-8
# 使用pandas进行转换
import pandas as pd

txt_path = 'student.txt'
excel_path = 'student.xls'
with open(txt_path) as f:
    s = eval(f.read(), {})
    for v in s.values():
        for i in range(len(v)):
            # 如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False。。
            if isinstance(v[i], basestring):
                v[i] = str(v[i]).decode('utf-8')

print s
s = pd.DataFrame(s).T
s.to_excel(excel_path, 'student', header=False)
