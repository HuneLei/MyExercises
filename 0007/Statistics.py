# -*- coding:utf-8 -*-
# 代码数量统计
import os


def stat_code():
    file_count, code_line_count, blank_line_count, comment_line_count = 0, 0, 0, 0
    files = os.walk('../../MyExercises')
    for (root, dirs, files) in files:
        for f in files:
            if f.endswith('.py'):
                file_count += 1
                with open(os.path.join(root, f), 'r') as cur_f:
                    for line in cur_f:
                        if line.strip().startswith('#'):  # 判断是否为注释
                            comment_line_count += 1
                        elif line.isspace():  # 判断是否是空行
                            blank_line_count += 1
                        else:
                            code_line_count += 1
    with open('count_code.txt', 'w') as f:
        f.write('文件数量：' + str(file_count) + '\n' + '代码行数：' + str(code_line_count) + '\n' \
                + '空行数量：' + str(blank_line_count) + '\n' + '注释数量：' + str(comment_line_count))


if __name__ == '__main__':
    stat_code()
