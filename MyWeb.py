# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@TIME: 2020/2/13 9:47
# !@Author : 提不动刀的胖虎
# !@File :.py

import web
from SQL import *

# 通过render方法渲染，先找到templates的文件夹


render = web.template.render("html")
urls = (
    "/login", "login",
    # "/home_page", "home_page"
)
app = web.application(urls, globals())


# 1.登录功能
class login:

    # 注意此处得GET要全大写和底下POST一样
    def GET(self):

        # 向服务器发起请求，是否存在login，存在即返回
        return render.login()
        pass

    # 从前端页面上发送得数据，来接收得方法，接受得信息与前端页面输入框内容一样
    def POST(self):

        loginUser = web.input()
        print("用户名：", loginUser.username, ",密码:", loginUser.password)

        data_base = ConnectSQL.Database()
        if data_base.Login(loginUser.username, loginUser.password):
            print("登录成功")
            return render.home_page()
            pass
        else:
            print("登录失败")
        pass

    pass


if __name__ == "__main__":
    app.run()
