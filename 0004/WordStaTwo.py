# -*- coding: utf-8 -*-

import re
from collections import Counter


def count_word(file='subtitle.txt'):
    with open(file, 'r') as f:  # with...as...可以省略close()操作
        count_list = Counter(re.split('\W+', f.read().lower().strip()))  # 通过Counter方法计数
        w = open('count_word.txt', 'w')
        word_list = ''
        for word, count in count_list.items():  # 循环一个元组
            if word != '':
                word_list = word_list + '%s, %d' % (word, count) + '\n'
        w.write(word_list)
        w.close()


if __name__ == '__main__':
    count_word()
