# -*- coding:utf-8 -*-
import urllib2
import urllib
import cookielib
import socket

url = 'https://www.cnblogs.com/sudawei/p/3345863.html'

# 基本用法
res = urllib2.urlopen(url)
# print res.read()

# 加上要get或post的数据
data = {'name': 'hank', 'passwd': 'hjz'}
res2 = urllib2.urlopen(url, urllib.urlencode(data))
# print res2.read()

# 加上http头
# header = {'User-Agent': 'Mozilla-Firefox5.0'}
# urllib2.urlopen(url, urllib.urlencode(data), header)

# 加上session
cj = cookielib.CookieJar()
cjhandler = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cjhandler)
urllib2.install_opener(opener)

# 加上Basic认证
username = 'wodota0909@163.com'
password = '******'
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.163.com/"
password_mgr.add_password(None, top_level_url, username, password)
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

# 使用代理
proxy_support = urllib2.ProxyHandler({'http': 'http://1.2.3.4:3128/'})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

# 设置超时
socket.setdefaulttimeout(5)
urllib2.urlopen(url, timeout=5)
