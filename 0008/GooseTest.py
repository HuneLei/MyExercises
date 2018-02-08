# -*- coding:utf-8 -*-
# pip install goose-extractor 下载goose库

from goose import Goose
from goose.text import StopWordsChinese

# url = 'https://zhuanlan.zhihu.com/p/26186637'
url = 'http://world.huanqiu.com/exclusive/2018-01/11561579.html'
g = Goose()

exclusive = g.extract(url=url)

print exclusive.title  # 获取网页的标题
print exclusive.domain  # 获取信息发布网址域名

g = Goose({'stopwords_class': StopWordsChinese})
exclusive = g.extract(url=url)

print exclusive.meta_keywords  # 获取网页关键字
print exclusive.meta_description  # 获取网页信息摘要
print exclusive.cleaned_text[:] # 获取网页信息详情
