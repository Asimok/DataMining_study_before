# -*- coding: utf-8 -*-
# author: Jclian91
# place: Pudong Shanghai
# time: 2020-02-12 12:57
import pandas as pd


# 读取txt文件
def read_txt_file(file_path):
    classification = ['城乡建设', '环境保护', '交通运输', '教育文体', '劳动和社会保障', '商贸旅游', '卫生计生']
    data_train = pd.read_excel(file_path, sheet_name='Sheet1')
    text_tr = []
    y_tr = []

    for i in data_train['留言详情']:
        text_tr.append(
            str(i).strip().replace(' ', '').replace('\n', '').replace('\t', '').replace('\u3000', '').replace('\xa0',
                                                                                                              ''))
    for i in data_train['一级分类']:
        y_tr.append(classification.index(i))
        # y_tr.append(i)

    return y_tr, text_tr


file_path = '/home/asimov/PycharmProjects/DataMining/MQ/深度学习/NLP/data/训练集.xlsx'
labels, texts = read_txt_file(file_path)
train_df = pd.DataFrame({'label': labels, 'text': texts})
print(len(texts))

file_path = '/home/asimov/PycharmProjects/DataMining/MQ/深度学习/NLP/data/测试集.xlsx'
labels, texts = read_txt_file(file_path)
test_df = pd.DataFrame({'label': labels, 'text': texts})

print(train_df.head())
print(test_df.head())

train_df['text_len'] = train_df['text'].apply(lambda x: len(x))
print(train_df.describe())



