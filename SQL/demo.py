from SQL import *
# 数据库名称
DName = 'hello'
mysql = ConnectSQL.Database()
mysql.Register('Admin','Admin')
mysql.Login('Admin','Admin')
mysql.Login('Admin','Admin1')
mysql.Login('Admin1','Admin1')
