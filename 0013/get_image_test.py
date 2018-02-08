# -*- coding: utf-8 -*-
import requests
import lxml.html

url = 'http://tieba.baidu.com/p/2166231880'
path = 'Image\\'
page = requests.get(url)
doc = lxml.html.document_fromstring(page.text)
# print page.text
for idx, el in enumerate(doc.cssselect('img.BDE_Image')):
    # '%03d',用于字符串格式化 '%d':输出一个数值变量 '%03d':输出一个数值变量,不足3位在前面补0
    with open(path + '%03d.jpg' % idx, 'wb') as f:
        f.write(requests.get(el.attrib['src']).content)
