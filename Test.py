# 数据库名称
from SQL import *

DName = 'hello'
mysql = ConnectSQL.Database()
CrawlData = DouBan.DouBan()
CrawlData.GetData()
mysql.CreateTable(
    "CREATE TABLE IF NOT EXISTS %s(carinfor char(20),school int,weater char(20),class int)" % DName)
mysql.CreateTable(CrawlData, DName)
