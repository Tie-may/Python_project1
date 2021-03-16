# 连接mysql数据库
import os
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy


class Database():
    def __init__(self):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='zxc123',
            charset='utf8mb4',
            database='mysql'
        )
        # 创建游标对象
        self.cur = conn.cursor()

    def CreateTable(self, ExecuteStr):
        # 创建数据表
        try:
            # create_sqli = "CREATE TABLE IF NOT EXISTS hello(carinfor char(20),school int,weater char(20),class int)"
            self.cur.execute(ExecuteStr)
        except Exception as e:
            print("创建表失败:", e)
        else:
            print("创建数据表成功;")

    def ToSql(self, DataSet, TableName):
        # 导入数据
        # index：索引关闭 if_exists: replace 表存在则删除再写入  fail:什么都不干
        # DataSet类型必须为pd类型
        engine = create_engine(
            'mysql+pymysql://root:zxc123@localhost/mysql?charset=utf8')
        DataSet.to_sql(TableName, engine, index=False, if_exists='append')
