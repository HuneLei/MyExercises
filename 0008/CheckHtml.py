# -*- coding: utf-8 -*-
# 一个HTML文件，找出里面的正文

import sys
from goose import Goose
from goose.text import StopWordsChinese

# UnicodeEncodeError: ‘ascii’ codec can’t encode异常错误解决方法
reload(sys)
sys.setdefaultencoding('utf-8')


def read_html(url='http://www.jianshu.com/p/05cfea46e4fd',
              url_file='2016年人工智能领域的总结与思考：未来将面临的五大考验 - 简书.html',
              open_url=False):
    # 方法以 encoding 指定的utf-8格式解码字符串
    with open(url_file.decode('utf8'), 'r') as f:
        words = f.read()
    g = Goose({'stopwords_class': StopWordsChinese})
    if open_url:
        article = g.extract(url=url)
    else:
        article = g.extract(raw_html=words)

    with open('goose_test.txt', 'w') as wr:
        wr.write(article.title.decode('utf8') + '\n' + article.cleaned_text[:])


if __name__ == '__main__':
    read_html('https://mp.weixin.qq.com/debug/wxadoc/dev/framework/config.html',
              open_url=True)
