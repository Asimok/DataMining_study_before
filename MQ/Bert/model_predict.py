# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from keras.models import load_model

from MQ.Bert.bert.extract_feature import BertVector

load_model = load_model("./model/model2.h5")
classification = ['城乡建设', '环境保护', '交通运输', '教育文体', '劳动和社会保障', '商贸旅游', '卫生计生']
file_path = '/home/asimov/PycharmProjects/DataMining/MQ/深度学习/NLP/data/测试集.xlsx'
data_train = pd.read_excel(file_path, sheet_name='Sheet1')
texts = []
y_tr = []

for i in data_train['留言详情']:
    texts.append(
        str(i).strip().replace(' ', '').replace('\n', '').replace('\t', '').replace('\u3000', '').replace('\xa0',
                                                                                                          ''))
for i in data_train['一级分类']:
    y_tr.append(classification.index(i))
    # y_tr.append(i)
labels = []

bert_model = BertVector(pooling_strategy="REDUCE_MEAN", max_seq_len=470)

# 对上述句子进行预测
for text in texts:
    # 将句子转换成向量
    vec = bert_model.encode([text])["encodes"][0]
    x_train = np.array([vec])

    # 模型预测
    predicted = load_model.predict(x_train)
    y = np.argmax(predicted[0])
    # print(y)
    # label = 'Y' if y else 'N'
    labels.append(y)

# for text,y_label, label in zip(texts, y_tr,labels):
#     print('%s\t%s\t%s' % (label, y_label,text))

df = pd.DataFrame({'留言': texts, "原始类别": y_tr,"预测类别":labels},columns=['留言', "原始类别","预测类别"])
print(df)
acc_right=0
for i in range(len(labels)):
    if labels[i]==y_tr[i]:
        acc_right+=1
print("准确度: ",acc_right/len(labels))
# df.to_excel('./data/result.xlsx', index=False)
