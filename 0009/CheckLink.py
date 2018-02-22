# -*- coding:utf-8 -*-
# 一个HTML文件，找出里面的链接。

from bs4 import BeautifulSoup
import urllib2


def gain_links(url='http://www.jianshu.com/p/05cfea46e4fd'):
    html_page = urllib2.urlopen(url)
    links = BeautifulSoup(html_page).findAll('a')
    links = [i.get('href') for i in links if i.get('href') and not i.get('href').startswith('javascript:')]
    proto, rest = urllib2.splittype(url)  # python提取url中的域名和端口号
    domain = urllib2.splithost(rest)[0]  # 获取url的host
    links = map(lambda i: proto + '://' + domain + i if i[0] == '/' else url + i if i[0] == '#' else i, links)  # 把链接补全
    with open('links_list.txt', 'w') as f:
        f.write('\n'.join(links))


if __name__ == '__main__':
    gain_links('https://www.zhihu.com/collection/140905871')
