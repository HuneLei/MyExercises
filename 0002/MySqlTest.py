# -*- coding: utf-8 -*-
import MySQLdb

db = MySQLdb.connect('localhost', 'root', '123456', 'sqltest', charset='utf8')
cursor = db.cursor()
# sql = "SELECT name FROM `new_table` \
#                 WHERE num > '%d'" % (20)

sql = "INSERT INTO new_table(id, NAME, num) VALUES ('%d', '%s', '%d')" % (5, '宝哥', 60)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
# cursor.execute(sql)
# data = cursor.fetchall()
# print data
db.close()
