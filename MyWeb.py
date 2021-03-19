# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@TIME: 2020/2/13 9:47
# !@Author : 提不动刀的胖虎
# !@File :.py

import web
from SQL import *
from crawler import*
# 通过render方法渲染，先找到templates的文件夹



render = web.template.render("html")
urls = (
    "/login","login",
    "/home_page","home_page",
    "/douban.html","douban",
    "/jd.html",'jd',
    "/novel.html","nv"
    # # login对应下面的类login。  "/login" 指的是跳转页面，用户表管理
    # "/login", "login",
    # "/showUser", "showUser",
    # "/toAddUser", "toAddUser",  # 跳转到增加页面
    # "/addUser", "addUser",   # 增加操作
    # "/delUser", "delUser",
    # "/toUpdateUser", "toUpdateUser",  # 跳转到修改页面
    #  "/updateUser", "updateUser",    # 作修改
    # "/findUserByNames", "findUserByNames",  # 全文搜索
    #
    #
    # # 爬虫的图书管理---------------
    # "/showCrawler", "showCrawler",  # 爬虫数据采集

)
app = web.application(urls, globals())
data_base = ConnectSQL.Database()

# 1.登录功能
class login:

    # 注意此处得GET要全大写和底下POST一样
    def GET(self):
        flag = True
        # 向服务器发起请求，是否存在login，存在即返回
        return render.login(flag)
        pass

    # 从前端页面上发送得数据，来接收得方法，接受得信息与前端页面输入框内容一样
    def POST(self):
        flag=False
        loginUser = web.input()
        print(loginUser)
        # print("用户名：", loginUser.username, ",密码:", loginUser.password)
        print(loginUser.keys())

        if loginUser.submit=='注册':
            print("注册")
            data_base.Register(loginUser.new_username,loginUser.new_password)
        elif loginUser.submit=='修改':
            if data_base.Modify(loginUser.old_username,loginUser.old_password,loginUser.modified_password):
                print("修改成功")
            else:
                print("修改失败")
                return render.login(flag)
        else:
            if data_base.Login(loginUser.username,loginUser.password):
                print("登录成功")
                return render.home_page()
                pass
            else :
                print("登录失败")
                return render.login(flag)
        pass
    pass

class home_page:
    def GET(self):
        return render.showUser()
        pass
    pass

class douban:
    def GET(self):
        return render.douban()
        pass
class nv:
    def GET(self):
        return render.nv()
        pass

class jd:
    def GET(self):
        data=[]
        return render.jd(data)
        pass

    def POST(self):
        table_name = 'jd'
        data=[]
        input = web.input()
        print(input)
        if (input.submit=="开始爬取"):
            crawl = JD.JD().get_data(input.search)
            print(crawl)
            data_base.UploadData(crawl, table_name)
            return render.jd(data)
        elif (input.submit=="分析结果"):
            print("停止")
        else:
            data=data_base.DownloadData(table_name)
            print(data)
            return render.jd(data)




# 2.2跳转到新增页面
# class toAddUser:
#
#     def GET(self):
#         return render.addUser()
#         pass
#
#     pass
#
# class addUser:
#
#     def POST(self):
#         newUser = web.input()
#         print("用户名：", newUser.username,"，密码：", newUser.password)
#         b = UserService().addUser(newUser)
#         if(b):
#             return web.seeother("showUser")
#             pass
#         else:
#             return web.seeother("error1")
#             pass
#         pass
#     pass
#
# # 2.3删除功能
#
# class delUser:
#
#     def GET(self):
#
#         id = web.input()
#         print(id)
#
#         # 因为从网页上流转的数据都是string类型,所以需要强制类型转换
#         b = UserService().deletUser(int(id.get("id")))
#         if(b):
#
#             return web.seeother("showUser")
#             pass
#         else:
#
#             return web.seeother("error1")
#             pass
#         pass
#     pass
#
# # 2.4跳转修改页面
# class toUpdateUser:
#
#     def GET(self):
#
#         id = web.input()
#         print(id)
#
#         oldUser = UserService().FindUserById(int(id.get("id")))
#
#         return render.updateUser(oldUser)
#         pass
#     pass

# 2.5作修改操作
# class updateUser:
#
#     def POST(self):
#
#         oldUser = web.input()
#
#         print(oldUser)
#         count = UserService().doUpdateUser(oldUser)
#
#         if(count>0):
#
#             return web.seeother("showUser")
#             pass
#
#         else:
#             return web.seeother("error1")
#             pass
#
#
#         pass
#
#     pass

# 2.6全文搜索
# class findUserByNames:
#
#     def POST(self):
#
#         searchName = web.input()
#         print(searchName)
#         print(searchName.searchName)
#         result = UserService().doFindUserByName(searchName.searchName)
#         print(result)
#         return render.showUser(result)
#
#         pass
#     pass



# 3.1 爬取数据，并显示

# class showCrawler:
#
#     def POST(self):
#
#         url = web.input()
#         print(url.geturl)
#
#         # 爬取数据
#         bookList = BookCrawler().getBookInfoCrawler(url.geturl)
#         # 存储数据
#         BookService().doSaveCrawlerDataToDB(bookList)
#
#         # 全查询数据
#         result = BookService().doFindAllBook()
#
#         return render.showCrawler(result)
#         pass
#
#     pass

if __name__ == "__main__":
    app.run()