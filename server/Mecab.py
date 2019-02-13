import MeCab
import MySQLdb
import os


def distribution(id, text):
    m = MeCab.Tagger()
    keywords = m.parse(text)

    for row in keywords.split('\n'):
        r = row.split('\t')
        word = r[0]
        if word == 'EOS':
            break
        else:
            pos = r[1].split(',')[0]
            if pos == '名詞':
                cursor2 = connection.cursor()
                insert_sql = "insert into WordList(anime_id, word) value(%s, %s)"
                cursor2.execute(insert_sql, (id, word))
                connection.commit()
                cursor2.close()


if __name__ == '__main__':
    connection = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd=os.environ['MYSQLPASS'],
                                 db='Anime', charset='utf8')
    select_sql = 'select id, outline from Anime'
    cursor1 = connection.cursor()
    cursor1.execute(select_sql)

    for row in cursor1:
        distribution(row[0], row[1])