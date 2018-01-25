# -*- coding:utf-8 -*-
from random import Random
import MySQLdb
import string


class random_sql:
    # 初始化方法
    def __init__(self, file='codes.txt'):
        self.code_list = []
        self.file = file

    # 生成数据的方法
    def create_code(self, code_num=10, code_len=8):
        str_code = string.digits + string.letters
        self.code_list = [''.join([Random().choice(str_code) for i in range(code_len)]) for j in range(code_num)]
        return self.code_list

    # 将数据保存到文件的方法
    def save_file(self):
        f = open(self.file, 'w')
        f.write('start\n' + '\n'.join(self.code_list) + '\nend')
        f.close()

    # 将数据保存到数据库的方法
    def save_sql(self, sql_code):
        # 连接数据库
        db = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='sqltest', charset='utf8')
        cursor = db.cursor()  # 获取光标
        try:
            # 创建表
            cre_sql = "CREATE TABLE code_list(id INT auto_increment PRIMARY KEY, sql_code VARCHAR(%d))" % (20)
            cursor.execute(cre_sql)
            db.commit()
        except:
            db.rollback()
        # 查询表中的数据
        sele_sql = "SELECT sql_code FROM `code_list`"
        cursor.execute(sele_sql)
        sql_data = set(h[0] for h in cursor.fetchall())
        results = list(set(sql_code))  # 将列表转换成集合然后转换成列表去重
        for k in results:
            try:
                if k not in sql_data:  # 先查看是否存在,然后添加到数据库
                    add_sql = "INSERT INTO code_list(sql_code) VALUES('%s')" % (k)
                    cursor.execute(add_sql)
                    db.commit()
            except:
                db.rollback()
        cursor.close()
        db.close()


if __name__ == '__main__':
    R_sql = random_sql()
    sql_code = R_sql.create_code(5, 20)
    R_sql.save_file()
    R_sql.save_sql(sql_code)
