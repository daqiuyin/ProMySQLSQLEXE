# -*- coding: utf-8 -*-

import configparser

class dbtab:
    def __init__(self,tabname):
        configfile = 'mysqlconfig.txt'
        config = configparser.ConfigParser()
        config.read(configfile)
        self.host =config.get(tabname, 'host')
        self.port =config.get(tabname, 'port')
        self.user =config.get(tabname, 'user')
        self.password=config.get(tabname, 'password')
        self.db=config.get(tabname, 'db')
        self.charset = config.get(tabname,'charset')

if __name__ == '__main__':
    dev=dbtab('221dev')
    print(dev.host)
    print(dev.port)
# @Time    : 2018/3/1 15:25
# @Auth    : DAQIUYIN
# @File    : confctr.py
# @SoftWare: PyCharm Community Edition