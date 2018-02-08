# -*- coding: utf-8 -*-
import sys, locale


class replace_word:
    def __init__(self):
        self.input_word = ''
        self.word_dict = {}
        self.out_string = 'Human Rights'

    def save_dict(self, file='filtered_words.txt'):
        with open(file) as f:
            for line in f:
                if not self.word_dict.has_key(line.strip()):
                    self.word_dict[line.strip()] = True

    def input_words(self):
        self.input_word = raw_input('请输入你要检验的句子：').decode(
            sys.stdin.encoding or locale.getpreferredencoding(True)).encode('utf-8')

    def find_input(self):
        for keys in self.word_dict.keys():
            error_index = self.input_word.find(keys)
            if error_index != -1:
                self.input_word = self.input_word.replace(keys, '*' * len(keys.decode('utf-8')))
        print self.input_word


go_in = True

if __name__ == '__main__':
    RE = replace_word()
    while go_in:
        RE.save_dict()
        RE.input_words()
        RE.find_input()
        go_in = False if raw_input('是否继续?(输入N退出)') == 'N' else True
