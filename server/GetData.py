import MySQLdb
import io
import os
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
from time import sleep

base_url = 'https://anime.dmkt-sp.jp/animestore/ci_pc?workId='
image_url = 'https://cs1.anime.dmkt-sp.jp/anime_kv/img'


def get_data():
    for i in range(20000, 30000):
        sleep(1)
        response_anime = requests.get(base_url + str(i))
        response_anime.encoding = 'UTF-8'
        response_anime = BeautifulSoup(response_anime.content, 'lxml')

        # アニメのあらすじを取得
        anime_outline_container = response_anime.find('div', class_='outlineContainer')
        anime_title_container = response_anime.find('title')

        if anime_outline_container:
            anime_outline = anime_outline_container.find('p')

            try:
                anime_outline = anime_outline.string
                anime_outline = anime_outline.replace('\n', '')

                big_number = str(i)[0:2]
                middle_number = str(i)[2:4]
                small_number = str(i)[4:5]

                anime_image_url = image_url + '/' + big_number + '/' + middle_number + '/' + small_number + '/' + str(i) + '_1_1.png'

                anime_title_container = anime_title_container.string
                anime_title = anime_title_container.replace(' ', '').replace('|アニメ動画見放題|dアニメストア', '').replace('\n', '')

                cursor = connection.cursor()
                insert_sql = "insert into Anime(title, outline, image, url) value(%s, %s, %s, %s)"
                cursor.execute(insert_sql, (anime_title, anime_outline, anime_image_url, base_url + str(i) ))
                connection.commit()
                cursor.close()
            except:
                pass
        print(i)




if __name__ == '__main__':
    connection = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd=os.environ['MYSQLPASS'],
                                 db='Anime', charset='utf8')
    get_data()

    connection.close()
