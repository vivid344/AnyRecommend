import requests
import io
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import MySQLdb
from time import sleep
import os

if __name__ == '__main__':
    connection = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd=os.environ['MYSQLPASS'],
                                 db='research_tmp', charset='utf8')
    get_data()