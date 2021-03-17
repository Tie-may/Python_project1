from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
class maoyan():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://maoyan.com/board/4')

    def get_data(self):
        movie_number=[]
        movie_link=[]
        movie_star=[]
        movie_name=[]
        movie_time=[]
        movies = self.driver.find_elements_by_class_name('movie-item-info')
        # print(movies)
        for movie in movies:
            movie_number.append(movie.find_element_by_css_selector('.star').text)

            movie_link.append(movie.find_element_by_tag_name('a').get_attribute('href'))

            movie_star.append(movie.find_element_by_css_selector('.star').text)

            movie_name.append(movie.find_element_by_tag_name('a').get_attribute('title'))

            movie_time.append(movie.find_element_by_css_selector('.releasetime').text)

            # msg = '''
            #             排行:%s
            #             电影名:%s
            #             链接:%s
            #             主演:%s
            #         ''' % ("NO." + str(i), movie_name, movie_link, movie_time, movie_star)
        return pd.DataFrame({'movie_name':movie_name,'movie_star':movie_star,'movie_time':movie_time,'movie_number':movie_number,'movie_link':movie_link})
            # print(msg)
            # with open(file='猫眼TOP100', mode='a', encoding='utf-8') as f:
            #     f.write(msg)

        # button = driver.find_element_by_partial_link_text("下一页")
        # button.click()
        # time.sleep(1)
        # get_movies(driver)
my=maoyan()
print(my.get_data())

