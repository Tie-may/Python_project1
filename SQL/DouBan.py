
# 1. 加载，模拟用户去访问

from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
movie_crew = []
movie_class = []
movie_rate = []
rating_num = []


class DouBan():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.douban.com/')

    def GetData(self):
        # 实现抓取
        self.driver.find_element_by_link_text('排行榜').click()
        self.driver.find_element_by_link_text('动画').click()
        sleep(1)
        for i in range(5):
            self.driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(1.5)
        movies = self.driver.find_elements_by_class_name('movie-content')
        for movie in movies:
            movie_name = movie.find_element_by_class_name(
                "movie-name").find_element_by_tag_name("a").text
            # movie_crew = movie.find_element_by_class_name("movie-crew").text
            try:
                movie_crew.append(
                    movie.find_element_by_class_name("movie-crew").text)
                # 原文是except NoSuchElementException, e:
            except Exception as e:
                movie_crew = ""
                print("Can't find")
            try:
                movie_class.append(
                    movie.find_element_by_class_name("movie-misc").text)
            except Exception as e:
                movie_class = ""
                print("Can't find")
            # movie_class = movie.find_element_by_class_name("movie-misc").text
            movie_rate.append(
                movie.find_element_by_class_name("comment-num").text)
            rating_num.append(
                movie.find_element_by_class_name("rating_num").text)

        CrawlData = {'Name': movie_name,
                     'Crew': movie_crew,
                     'Class': movie_class,
                     'Rate': movie_rate,
                     'RateNum': rating_num
                     }

        return CrawlData
