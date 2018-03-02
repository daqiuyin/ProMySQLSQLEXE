# -*- coding: utf-8 -*-
import pymysql
from confctr import dbtab

class mysqlconnect:
    def __init__(self,host,port,user,password,db,charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.errmes=''
        self.execmes=''
        if charset :
            self.charset = charset
        else:
            self.charset = 'utf8'

    def exsql(self,sqltext,expect_count):
        self.sqltext = sqltext
        self.expect_count = expect_count
        connection = pymysql.connect(host=self.host,
                                     user=self.user,
                                     password=self.password,
                                     db=self.db,
                                     charset=self.charset,
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                self.row_count = cursor.execute(self.sqltext)

                if self.row_count == self.expect_count:
                    connection.commit()
                    self.execmes = '执行成功！\nsql：'+self.sqltext+ '\n影响条数为：%s'%self.row_count
                else:
                    self.errmes = '执行失败！实际执行条数（%s）与期望不一致（%s）' % (self.row_count, self.expect_count)
                    connection.rollback()


        except Exception as exceptmes:
            self.errmes = exceptmes
            self.execmes = self.execmes+'执行失败！\nsql：'+self.sqltext+'\n错误信息为：'+self.errmes




if __name__ == '__main__':
    def run_sql():
        dev = dbtab('221dev')
        mycon = mysqlconnect(host=dev.host, port=dev.port, user=dev.user, password=dev.password, db=dev.db,
                             charset=dev.charset)
        # mycon.exsql("insert into test_tb values ('1','kk');",1)
        mycon.exsql("update test_tb set name = 'kk002' where id  = 1 ;", 8)
        print(mycon.execmes)
        print(mycon.errmes)
    run_sql()


# @Time    : 2018/2/28 14:41
# @Auth    : DAQIUYIN
# @File    : mysqlconnect.py
# @SoftWare: PyCharm Community Edition