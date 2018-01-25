# -*- coding: utf-8 -*-
from random import Random
import string


class random_code:
    def __init__(self, file='codes.txt'):
        self.code_list = []
        self.file = file

    def get_code_list(self, number=10, code_len=8):
        str_code = string.letters + string.digits
        if type(code_len) != int or type(number) != int:
            print 'Invalid character'
        else:
            for j in range(number):
                self.code_list.append(''.join([Random().choice(str_code) for i in range(code_len)]))

    def save_code_file(self):
        f = open(self.file, 'w')
        f.write('start\n' + '\n'.join(self.code_list) + '\nend')
        f.close()


if __name__ == '__main__':
    R = random_code('class_codes.txt')
    R.get_code_list(200, 15)
    R.save_code_file()
