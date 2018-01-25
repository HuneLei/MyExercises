# -*- coding:utf-8 -*-
import re


def count_word(file='subtitle.txt'):
    f = open(file, 'r')
    w = open('count_word.txt', 'w')
    word_list = {}
    for line in f:
        line_list = re.split('\W+', line.lower().strip(''))  # 全部转换成小写字母且去首位空格)
        for word in line_list:
            if word in word_list:
                word_list[word] += 1
            elif word != '':
                word_list[word] = 1

    sort_list = sorted(word_list.items(), key=lambda x: x[1], reverse=True)
    english_word = '\n'.join(['word:%s, count:%d' % count_num for count_num in sort_list])
    w.write(english_word)
    w.close()
    f.close()


if __name__ == '__main__':
    count_word()
