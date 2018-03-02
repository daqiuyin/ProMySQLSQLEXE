# -*- coding: utf-8 -*-

import os
import sys

def ansqltest(sqlfile):
    sqllist=[]
    pathbef =os.path.join(sys.path[0],sqlfile)
    sqlwhoname = os.listdir(pathbef )
    #print(sqlwhoname)
    for i in sqlwhoname:
        with open(os.path.join(pathbef,i),'r') as sqltext:
            sqltextwh = sqltext.read()
            sqllist.extend(sqltextwh.split(';'))
    return sqlwhoname,sqllist


if __name__ == '__main__':
    print(ansqltest('sql'))



# @Time    : 2018/3/1 15:25
# @Auth    : DAQIUYIN
# @File    : ansqltest.py
# @SoftWare: PyCharm Community Edition