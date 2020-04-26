"""
数据预处理
分词
去停用词
"""
import re
import jieba
import pandas as pd


# file = './data/训练集.xlsx'
def data_process(file='./data/训练集.xlsx'):
    classification = ['城乡建设', '环境保护', '交通运输', '教育文体', '劳动和社会保障', '商贸旅游', '卫生计生']
    data_train = pd.read_excel(file)
    data_msg_detail = data_train['留言详情']
    data_msg_theme = data_train['留言主题']
    data_labels = data_train['一级分类']
    labels_all = []
    for i in data_labels:
        labels_all.append(classification.index(i))
    # 合并留言主题 和留言详情
    data_train['留言合并'] = data_msg_detail + data_msg_theme
    # 去除 \t \n
    data_all = data_train['留言合并'].apply(lambda x: re.sub('\n', '', re.sub('\t', '', x)))
    # jieba 分词
    jieba.load_userdict('./data/userdict1.txt')
    jieba.load_userdict('./data/weibo_jieba.txt')
    data_cut = data_all.apply(lambda x: jieba.lcut(x))
    # 去除停用词 csv 默认 ,作为分隔符 用sep取一个数据里不存在的字符作为分隔符保障顺利读取
    stop_words = pd.read_csv('data/stopword.txt', sep='hhhh', encoding='GB18030')
    # pd转列表拼接  iloc[:,0] 取第0列
    stop_words = list(stop_words.iloc[:, 0]) + [' ', '...', '', '  ', '→', '-', '：', ' ●', '\t', '\n']
    stop_words2 = pd.read_csv('data/userdict1.txt', sep='hhhh')
    data_after_stop = data_cut.apply(lambda x: [i.strip() for i in x if i not in stop_words])
    # data_after_stop = data_after_stop.apply(lambda x: [i.strip() for i in x if i not in list(stop_words2.iloc[:, 0])])
    # 去除空格
    data_after_stop = data_after_stop.apply(lambda x: [i for i in x if i != ''])
    # 空格分割字符
    data_str = data_after_stop.apply(lambda x: ' '.join(x))
    return data_str, data_after_stop, labels_all
