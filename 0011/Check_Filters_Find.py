# -*- coding: utf-8 -*-
class find_code:
    def __init__(self):
        self.words_dict = {}
        self.input_word = ''
        self.out_string = 'Human Rights'

    def open_file(self, file='filtered_words.txt'):
        with open(file) as f:
            for line in f:
                if not self.words_dict.has_key(line.strip()):
                    self.words_dict[line.strip()] = True

    def user_input(self):
        self.input_word = raw_input('请输入要校验的句子：')

    def find_word(self):
        for w in self.words_dict.keys():
            if self.input_word.find(w) != -1:
                self.out_string = 'Freedom'
                break
        print self.out_string


go_on = True

if __name__ == '__main__':
    while go_on:
        find = find_code()
        find.open_file()
        find.user_input()
        find.find_word()
        go_on = False if raw_input('是否继续(输入N退出)：') == 'N' else True
