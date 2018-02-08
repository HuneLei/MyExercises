# -*- coding:utf-8 -*-
import os
import re
from collections import Counter


def check_dirs(dir='MyDiary', save='count.txt'):
    files = os.walk(dir)
    for (root, dirs, files) in files:
        count_list = []
        for f in files:
            path = os.path.join(root, f)
            with open(path, 'r') as file:
                count_list += re.split('\W+', file.read().lower().strip())
        w = open(save, 'w')
        word_list = ''
        sort_list = sorted((Counter(count_list)).items(), key=lambda x: x[1], reverse=True)
        for word, count in sort_list:
            if word != '':
                word_list = word_list + '%s, %d' % (word, count) + '\n'
        w.write(word_list)
        w.close()


if __name__ == '__main__':
    check_dirs()
