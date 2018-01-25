# -*- coding: utf-8 -*-

from random import Random
import string

# chars = 'abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPGRSTUVWXYZ1234567890'
chars = string.letters + string.digits


def random_code(number=10, codelenth=8, file='codes.txt'):
    f = open(file, 'w')
    if number <= 0:
        print 'invalid number of codes'
    else:
        code_list = [''.join(Random().sample(chars, codelenth)) for i in range(number)]
        f.write('start\n' + str('\n'.join(code_list)) + '\nend')
        f.close()


if __name__ == '__main__':
    random_code(1000, 12)
