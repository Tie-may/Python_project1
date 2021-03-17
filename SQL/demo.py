# 接口示例
from SQL import *
mysql = ConnectSQL.Database()
mysql.Register('Admin','Admin')#Register 返回布尔值 除成功注册外返回False 下同
mysql.Login('Admin','Admin')
mysql.Login('Admin','Admin1')
mysql.Login('Admin1','Admin1')


