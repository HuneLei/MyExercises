# -*- coding: utf-8 -*-
import sys, locale

filtered_words = 'filtered_words.txt'
filtered_words_dict = {}
with open(filtered_words) as f:
    for line in f:
        word = line.strip()  # 去首尾空格
        if not filtered_words_dict.has_key(word):
            # word = json.dumps(word, encoding='UTF-8', ensure_ascii=False)
            filtered_words_dict[word] = True

while True:
    # input()输入严格按照Python的语法,是字符就自觉的加 ' ',数字就是数字~
    # 系统编码： 默认编码，正常情况下window系统默认是gbk, linux系统默认是utf - 8，可用locale.getdefaultlocale()
    # 和locale.setdefaultlocale()
    # 来控制，与encode有关
    #
    # 代码编码：python代码中的编码，默认是ascii，可用
    # "# -*- coding: utf-8 -*-"
    # 这种方式指定。python默认编码可用sys.getdefaultencoding()
    # 和sys.setdefaultencoding()
    # 来控制
    #
    # 文件编码：sys.getfilesystemencoding()
    #
    # 终端输入编码：sys.stdin.encoding
    #
    # 终端输出编码：sys.stdout.encoding，必须与locale编码保持一致，才能print出正确str
    if filtered_words_dict.has_key(raw_input().decode(sys.stdin.encoding or
                                                      locale.getpreferredencoding(True)).encode('utf-8')):
        print 'Freedom'
    else:
        print 'Human Rights'
