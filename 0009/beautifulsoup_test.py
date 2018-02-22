# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)

# prettify()格式化打印出了它的内容，这个函数经常用到
# print soup.prettify()

# 获取 Tags
# print soup.title

# 获取 head
# print soup.head

# 获取 a
# print soup.a

# 获取 p
# print soup.p

# soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称。
# print soup.name
# print soup.head.name

# print soup.p.attrs
# 在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。
# 如果我们想要单独获取某个属性，可以这样，例如我们获取它的 class 叫什么
# print soup.p['class']
# 还可以这样，利用 get 方法，传入属性的名称，二者是等价的
# print soup.p.get('class')

# 获取标签里面的内容
# print soup.p.string

# 查找所有得到相关节点
# print soup.findAll('p')
