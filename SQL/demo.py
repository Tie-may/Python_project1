# 接口示例
from crawler import *
from SQL import *


print("yes")
mysql = ConnectSQL.Database()
mysql.Register('Admin','Admin')#Register 返回布尔值 除成功注册外返回False 下同
mysql.Login('Admin','Admin')
mysql.Login('Admin','Admin1')
mysql.Login('Admin1','Admin1')
# crawl= JD.JD().get_data('显卡')
# crawl= DouBan.DouBan().GetData()
# crawl= maoyan.maoyan().get_data()
crawl=novel.novel().get_data()
print(crawl.size)
# print(crawl.columns.values)
# print(crawl.iloc[2].values)
table_name='test1'
print(crawl)
mysql.UploadData(crawl,table_name)
sql_data=mysql.DownloadData(table_name)
print(len(sql_data))

