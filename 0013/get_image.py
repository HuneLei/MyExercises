# -*- coding: utf-8 -*-
import requests

r = requests.get('http://settle.develop.api.wei3dian.com/member/settle/account/list',
                 {'access_token': 'ecaf5156-dbf8-459c-9bcd-fc404ed012b4', 'page': '0', 'size': '20'})

# GET请求
# r.text 返回headers中的编码解析的结果，可以通过r.encoding = 'gbk'来变更解码方式
# r.content返回二进制结果
# r.json()返回JSON格式，可能抛出异常
# 将结果保存到文件，利用r.iter_content()
# r.raw返回原始socket respons，需要加参数stream=True
# 传递headers
#
# >> > headers = {'user-agent': 'my-app/0.0.1'}
# >> > r = requests.get(url, headers=headers)
#
# 传递cookies
#
# >> > url = 'http://httpbin.org/cookies'
#
# >> > r = requests.get(url, cookies=dict(cookies_are='working'))
# >> > r.text
# '{"cookies": {"cookies_are": "working"}}'
print r.url
# print r.text
# print r.content
# print r.json()
print r.iter_content()

with open('raed.txt', 'wb') as fd:
    for chunk in r.iter_content(1000):  # 里面参数是分段写入文件
        fd.write(chunk)


# POST请求