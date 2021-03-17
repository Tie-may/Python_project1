from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

class JD():
    def __init__(self):
        # 1.定义浏览器
        self.driver = webdriver.Chrome()

        # 2.输入京东网址
        self.driver.get('https://www.jd.com/')


    def get_goods(self,search_obj):
        # 二。定位商品，抓取数据
        # 1.分析网页当前口罩的分页列表，所有口罩的商品都展现在<li>标签中，这些不同分类的口罩商品的<li>标签的属性class="gl-item"都是一样的，所以我们去定位商品，选class属性去定位
        # 3.定位输入关键字的搜索框，通过id来选定 id ='key'
        input_tag = self.driver.find_element_by_id('key')

        # 模拟键盘输入，输入关键字
        input_tag.send_keys(search_obj)

        # 点击确定，回车键
        input_tag.send_keys(Keys.ENTER)

        # 设置加载时间,目的让网页加载
        time.sleep(5)
        goods = self.driver.find_elements_by_class_name('gl-item')  # 查找多个节点，返回是个列表
        good_link=[]
        good_name=[]
        good_price=[]
        good_commit=[]
        # print(type(goods))
        # # # print(goods)

        # for循环取出商品：名字，价格，评论，商品的链接
        for good in goods:
            # 获取商品的链接：链接在<a>标签的href属性只不过
            good_link.append(good.find_element_by_tag_name('a').get_attribute('href'))

            # 获取商品名字：在<div class ='p-name'>下的<a>标签下的<em>标签中，但是会发现当前的商品名字分三段展示，所以运用replace函数用空白代替换行
            good_name.append(good.find_element_by_css_selector('.p-name em').text.replace('\n', ''))

            # 获取价格：同上可得
            good_price.append(good.find_element_by_css_selector('.p-price i').text)
            # 获取评论
            good_commit.append(good.find_element_by_css_selector('.p-commit a').text)
        return pd.DataFrame({'good_name':good_name,'good_price':good_price,'good_commit':good_price,'good_line':good_link})
        # # 抓取大量数据
        # button = driver.find_element_by_partial_link_text("下一页")
        # # 点击加载
        # button.click()
        # # 加载网页时间
        # time.sleep(1)



