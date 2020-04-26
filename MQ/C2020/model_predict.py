from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import GaussianNB

from MQ.C2020.data_process import data_process

classification = ['城乡建设', '环境保护', '交通运输', '教育文体', '劳动和社会保障', '商贸旅游', '卫生计生']
data_str_train, data_after_stop_train, labels_train = data_process(file='./data/训练集1.xls')
data_str_test, data_after_stop_test, labels_test = data_process(file='./data/测试集1.xls')
# data_after_stop_test.value_counts()
# 文本转换成词频
vectorizer = CountVectorizer()
# 词频转换成权值矩阵
transformer = TfidfTransformer()

"""
训练集样本
转成词向量
"""
count_tr = vectorizer.fit_transform(data_str_train).toarray()
"""
权值矩阵
"""
tfidf_tr = transformer.fit_transform(count_tr).toarray()

"""
测试集样本
转成词向量
CountVectorizer(vocabulary=vectorizer.vocabulary_)保证测试集和训练集单词个数一致
"""
count_te = CountVectorizer(vocabulary=vectorizer.vocabulary_).fit_transform(data_str_test).toarray()
"""
权值矩阵
转成tf-idf权值
"""
tfidf_te = transformer.fit_transform(count_te).toarray()

# 高斯朴素贝叶斯模型
model = GaussianNB()
# 模型训练
model.fit(tfidf_tr, labels_train)
# 模型预测
ans = model.predict(tfidf_te)
acr = model.score(tfidf_te, labels_test)
print("精度：", acr)
print("真实数据      预测数据")
for i, j in zip(labels_test, ans):
    print(classification[int(i)], "   ", classification[int(j)])
# 统计词频
dic = {}
for i in data_after_stop_train:
    for j in i:
        if j not in dic.keys():
            dic[j] = 1
        else:
            dic[j] += 1
