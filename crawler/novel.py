import requests
import parsel
import pandas as pd

class novel():
    def __init__(self):
        self.novel_list=[]

    def get_data(self):
        # 获取所有小说排行榜的网址
        names=[]
        urls=[]
        response = requests.get('http://www.xbiquge.la/xiaoshuodaquan/')

        # 防止乱码出现
        response.encoding = response.apparent_encoding

        sel = parsel.Selector(response.text)

        # 开始抓取小说网址
        dd_a = sel.css('li > a::attr(href)')
        url_s = dd_a.getall()

        for url in url_s[12:]:
            response = requests.get(url)

            # 防止乱码出现
            response.encoding = response.apparent_encoding
            sel = parsel.Selector(response.text)
            # 6.开始抓取章节网址
            dd_b = sel.css('h1::text')
            name = dd_b.get()
            novel_dict = {}
            names.append(name)
            urls.append(url)

        return pd.DataFrame({'name':names,'url':urls})

novel=novel()
print(novel.get_data())