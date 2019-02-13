import MySQLdb
from collections import defaultdict
import gensim
import MeCab
from gensim import corpora, models
import pandas as pd
import matplotlib.pyplot as plt
import os
from IPython.display import display

topic_N = 20
filename = 'tmp/lda_' + str(topic_N) + '.model'


def delete_one_time(words_list):
    frequency = defaultdict(int)
    for text in words_list:
        for token in text:
            frequency[token] += 1
    words_list = [[token for token in text if frequency[token] > 1] for text in words_list]
    return words_list


def make_dict(word_list):
    dictionary = corpora.Dictionary(word_list)
    dictionary.save('tmp/deerwester.dict')
    dictionary.save_as_text('tmp/deerwester.dict.txt')
    return dictionary


def make_corpus(dict, word_list):
    corpus = [dict.doc2bow(text) for text in word_list]
    corpora.MmCorpus.serialize('tmp/deerwester.mm', corpus)
    return make_lda(corpus, dict)


def coherence(corpus, dict):
    lda = None
    # コヒーレンス描画のための初期化
    output_list = pd.DataFrame(columns=["y", "x"])
    plt.ion()
    fig = plt.figure()
    axe = fig.add_subplot(111)

    for i in range(2, 300):
        lda = gensim.models.ldamodel.LdaModel(corpus=corpus, num_topics=i, id2word=dict)
        lda.save(filename)

        cm = models.coherencemodel.CoherenceModel(model=lda, corpus=corpus,
                                                  coherence='u_mass')  # tm is the trained topic model

        # コヒーレンスのグラフ描画
        d = {'y': cm.get_coherence(), 'x': i}
        df = pd.DataFrame(data=d, index=[0])
        output_list = output_list.append(df)

        axe.cla()
        axe.plot(output_list.x, output_list.y)
        fig.set_size_inches(8, 8)
        display(fig)

    return lda


def specified_number(corpus, dict):
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, num_topics=topic_N, id2word=dict)
    lda.save(filename)

    for i in range(topic_N):
        print("\n")
        print("=" * 80)
        print("TOPIC {0}\n".format(i))
        topic = lda.show_topic(i)
        for t in topic:
            print("{0:20s}{1}".format(t[0], t[1]))

    return lda


def make_lda(corpus, dict):
    lda = specified_number(corpus, dict)
    # lda = coherence(corpus, dict)
    return lda


def noun():
    word_lists = []

    cate_sql = 'select id from Anime'
    cursor1 = connection.cursor()
    cursor1.execute(cate_sql,)

    for row1 in cursor1:
        word_list = []
        select_sql = 'select word from WordList where anime_id = %s'
        cursor2 = connection.cursor()
        cursor2.execute(select_sql, (row1[0], ))

        for row2 in cursor2:
            if len(row2[0]) > 1 and not row2[0].isdigit():
                if row2[0] != 'こと' and row2[0] != 'ため' and row2[0] != 'さん' and row2[0] != 'これ' and row2[0] != 'よう' \
                        and row2[0] != 'たち' and row2[0] != 'もの' and row2[0] != 'None':
                    word_list.append(row2[0])
        word_lists.append(word_list)

    dict = make_dict(delete_one_time(word_lists))
    # dict_lists.append(make_corpus(dict, word_lists))

    return make_corpus(dict, word_lists), dict

# def test_data(lda, dict):
#     print('Input Yahoo News URL:')
#     i = input()
#     text = GetNews.get_news_text(i)
#     m = MeCab.Tagger()
#     keywords = m.parse(text)
#     test_word_list = []
#     test_word_lists = []
#     for row in keywords.split('\n'):
#         r = row.split('\t')
#         word = r[0]
#         if word == 'EOS':
#             break
#         else:
#             pos = r[1].split(',')[0]
#             if pos == '名詞':
#                 test_word_list.append(word)
#
#     test_word_lists.append(test_word_list)
#     test_corpus = [dict.doc2bow(text) for text in test_word_lists]
#
#     for topics_per_document in lda[test_corpus]:
#         print(topics_per_document)


if __name__ == '__main__':
    connection = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd=os.environ['MYSQLPASS'],
                                 db='Anime', charset='utf8')
    lda = noun()
    for i in range(topic_N):
        print("\n")
        print("=" * 80)
        print("TOPIC {0}\n".format(i))
        topic = lda[0].show_topic(i)
        for t in topic:
            print("{0:20s}{1}".format(t[0], t[1]))

    # while True:
    #     print('Use Existing Model? (y or n)')
    #     i = input()
    #     if i == 'n':
    #         while True:
    #             print('Create New Model? (y or n)')
    #             j = input()
    #             if j == 'n':
    #                 break
    #             elif j == 'y':
    #                 lda = noun()
    #                 break
    #             else:
    #                 print('Type y or n \n')
    #     elif i == 'y':
    #         lda = gensim.models.LdaModel.load('tmp/lda.model'), gensim.corpora.Dictionary.load('tmp/deerwester.dict')
    #         # 既存モデルのトピック表示
    #         for i in range(topic_N):
    #             print("\n")
    #             print("=" * 80)
    #             print("TOPIC {0}\n".format(i))
    #             topic = lda[0].show_topic(i)
    #             for t in topic:
    #                 print("{0:20s}{1}".format(t[0], t[1]))
    #         break
    #     else:
    #         print('Type y or n \n')

    connection.close()
    # while True:
    #     test_data(lda[0], lda[1])


