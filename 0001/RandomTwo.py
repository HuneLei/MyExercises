# -*- coding: utf-8 -*-#
from random import Random

chars = 'abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPGRSTUVWXYZ1234567890'


def random_code(number=10, codelenth=8, file='codes.txt'):
    f = open(file, 'w')
    f.write('start\n')
    chars_lenth = len(chars)
    if number <= 0:
        print 'invalid number of codes'
    for i in range(number):
        str = ''
        for y in range(codelenth):
            random_num = Random().randint(1, chars_lenth)
            str = str + chars[random_num - 1]
        f.write(str + '\n')
    f.write('end')
    f.close()


if __name__ == '__main__':
    random_code(1000, 12)
