import MeCab
import MySQLdb
import os


def distribution(id, text, stopwords_ja, stopwords_en):
    m = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/")
    keywords = m.parse(text)

    for row in keywords.split('\n'):
        r = row.split('\t')
        word = r[0]
        if word == 'EOS':
            break
        else:
            pos = r[3].split('-')[0]
            if pos == '名詞':
                if word not in stopwords_ja and word not in stopwords_en:
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

    # 日本語のstopword
    stopwords_ja = []
    f1 = open('./txt/Japanese.txt')
    data1 = f1.read()
    f1.close()

    lines1 = data1.split('\n')

    for line in lines1:
        if line:
            stopwords_ja.append(line)

    # 英語のstopword
    stopwords_en = []
    f2 = open('./txt/English.txt')
    data2 = f2.read()
    f2.close()

    lines2 = data2.split('\n')

    for line in lines2:
        if line:
            stopwords_en.append(line)

    for row in cursor1:
        distribution(row[0], row[1], stopwords_ja, stopwords_en)