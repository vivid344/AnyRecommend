import os

import MySQLdb
from gensim import corpora, models
import gensim

topic_N = 15


def corpus(d, word_lists):
    return [d.doc2bow(text) for text in word_lists]


def make_dict_corpus():
    cate_sql = 'select id from Anime'
    cursor1 = connection.cursor()
    cursor1.execute(cate_sql, )
    word_lists = []

    for row1 in cursor1:
        word_list = []
        select_sql = 'select word from WordList where anime_id = %s'
        cursor2 = connection.cursor()
        cursor2.execute(select_sql, (row1[0],))

        for row2 in cursor2:
            if len(row2[0]) > 1 and not row2[0].isdigit():
                word_list.append(row2[0])
                word_lists.append(word_list)

    d = corpora.Dictionary(word_lists)
    d.filter_extremes(no_below=5)
    d.save('tmp/deerwester.dict')
    print('dict done!')

    c = corpus(d, word_lists)
    gensim.corpora.MmCorpus.serialize('tmp/corpus.mm', c)  # 保存
    print('corpus done!')

    lda = models.ldamodel.LdaModel(corpus=c, id2word=d, num_topics=topic_N, passes=10)
    lda.save('./tmp/lda_50.model')
    print('model done!')

    for i in range(topic_N):
        print("\n")
        print("=" * 80)
        print("TOPIC {0}\n".format(i))
        topic = lda.show_topic(i)
        for t in topic:
            print("{0:20s}{1}".format(t[0], t[1]))


if __name__ == '__main__':
    connection = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd=os.environ['MYSQLPASS'],
                                 db='Anime', charset='utf8')

    make_dict_corpus()
