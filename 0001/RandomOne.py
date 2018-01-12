# -*- coding: utf-8 -*-
import uuid


def creat_uuid(num=10, file='uuid.txt'):
    f = open(file, 'w')
    array_uuid = [str(uuid.uuid1()).replace('-', '') for i in xrange(100)]
    s = '\n'
    f.write('生成' + str(num) + '个UUID:\n' + s.join(array_uuid))
    # f.write(str(array_uuid).replace(',', '\n'))
    f.close()


if __name__ == '__main__':
    creat_uuid(200)
