# 接口示例
from SQL import *
import pandas as pd
from sqlalchemy import create_engine
mysql = ConnectSQL.Database()
mysql.Register('Admin','Admin')#Register 返回布尔值 除成功注册外返回False 下同
mysql.Login('Admin','Admin')
mysql.Login('Admin','Admin1')
mysql.Login('Admin1','Admin1')
crawl=DouBan.DouBan().GetData()
print(crawl.size)
# print(crawl.columns.values)
# print(crawl.iloc[2].values)
table_name='test2'
print(crawl)
mysql.UploadData(crawl,table_name)
sql_data=mysql.DownloadData(table_name)
print(len(sql_data))

