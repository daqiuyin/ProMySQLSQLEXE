# -*- coding: utf-8 -*-
from ansqltest import ansqltest
import mysqlconnect
import confctr


def run_sql():
    sqlfincont=[]
    dbname = input('选择数据库：默认为221dev\n')
    if not dbname:
        dbname = '221dev'
    dev = confctr.dbtab(dbname)
    mycon = mysqlconnect.mysqlconnect(host=dev.host,port=dev.port,user=dev.user,password=dev.password,db=dev.db,charset=dev.charset)

    filename= input('脚本所在的文件位置：默认为sql\n')
    if not filename:
        filename = 'sql'
    expectcon = input('请输入预测结果，以,分隔:\n').split(',')
    sqlandcont = ansqltest(filename)
    print('需要执行的文件为：')
    for i in sqlandcont[0]:
        print(i)
    print('需要执行的sql为：')
    for i in sqlandcont[1]:
        if i:
            print(i)
            sqlfincont.append(i)
    if not input():
     for i in range(len(sqlfincont)):
             mycon.exsql(sqlfincont[i]+';',int(expectcon[i]))
             print(mycon.execmes)
             print(mycon.errmes)


if __name__ == '__main__':
    run_sql()


# @Time    : 2018/3/2 10:52
# @Auth    : DAQIUYIN
# @File    : execmain.py
# @SoftWare: PyCharm Community Edition