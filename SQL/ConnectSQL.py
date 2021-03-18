# 连接mysql数据库
import os
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
from .SqlConfig import *


class Database():
    def __init__(self):
        self.conn = pymysql.connect(
            host=sql_host,
            user=sql_user,
            password=sql_password,
            charset='utf8mb4',
            database=sql_database
        )
        # 创建游标对象
        self.cur = self.conn.cursor()
        # self.cur.execute("DROP TABLE User")
        self.cur.execute("CREATE TABLE IF NOT EXISTS user(username char(20),password char(20))")

    def GetSql(self, SqlStr):
        self.cur.execute(SqlStr)
        result = self.cur.fetchone()
        return result

    def CreateTable(self, ExecuteStr,table_name):
        # 创建数据表
        try:
            # create_sqli = "CREATE TABLE IF NOT EXISTS hello(carinfor char(20),school int,weater char(20),class int)"
            self.cur.execute('DROP TABLE IF EXISTS %s'%table_name)
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
            # 'mysql+pymysql://root:zxc123@localhost/%s?charset=utf8'%(sql_password))
            'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (sql_user,sql_password,sql_host,sql_database))
        DataSet.to_sql(TableName, engine, index=False, if_exists='append')

    def Login(self, username, password):
        # 判断数据库中是否含有相关用户并检测密码是否正确
        sqlStr = "SELECT password FROM User WHERE username = '%s'" % username
        Infor = self.GetSql(sqlStr)
        # 判断返回值是否为NULL
        if Infor:
            flag = True
        else:
            flag = False
        if (flag):
            if (Infor[0] == password):
                print("登录成功")
                return True
            else:
                print("密码错误")
                return False
        else:
            print("用户名不存在")
            return False

    def Register(self, username, password):
        # 注册用户
        # 返回布尔值 成功注册返回True 错误返回False
        SqlStr = "SELECT * FROM User WHERE username = '%s'" % username
        if self.GetSql(SqlStr):
            print("用户名已存在")
            return False
        else:
            self.cur.execute("INSERT INTO User (username,password) VALUE ('%s','%s')" % (username, password))
            print("成功注册")
            return True

    def Modify(self,username,oldpassword,newpassword):
        SqlStr = "SELECT * FROM user WHERE username = '%s'"%username
        demo=self.GetSql(SqlStr)
        if demo:
            if demo[0]==oldpassword:
                self.cur.execute("UPDATE user SET password = '%s' WHERE username = '%s'")%(newpassword,username)
                return True
            else:
                print("用户名错误")
                return False
        else:
            print("未找到用户名")
            return False


    def UploadData(self,crawl_data,table_name):
        demo = crawl_data.iloc[2].values
        colum_name = crawl_data.columns.values
        sql_str = 'CREATE TABLE %s(' % table_name
        for i in range(len(demo)):
            crawl_name = colum_name[i]
            crawl_value = demo[i]
            if isinstance(crawl_value, int):
                sql_str = sql_str + '%s INT' % colum_name[i]
            elif isinstance(crawl_value, float):
                sql_str = sql_str + '%s FLOAT' % colum_name[i]
            elif isinstance(crawl_value, str):
                sql_str = sql_str + '%s VARCHAR(2000)' % colum_name[i]
            sql_str = sql_str + ','
        sql_str = sql_str[:-1] + ')'
        self.CreateTable(sql_str, table_name)
        self.ToSql(crawl_data,table_name)

    def DownloadData(self,table_name):
        sql_str='SELECT * FROM %s'%table_name
        self.cur.execute(sql_str)
        down_data=self.cur.fetchall()
        return down_data