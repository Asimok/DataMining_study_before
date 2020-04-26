import jieba
import pandas as pd

"""
训练集处理
"""
classification = ['城乡建设', '环境保护', '交通运输', '教育文体', '劳动和社会保障', '商贸旅游', '卫生计生']
data = pd.read_excel('/home/asimov/PycharmProjects/DataMining/C_data/附件2.xlsx', sheet_name='Sheet1')
test = []
y_test = []
train = []
y_train = []
dev = []
y_dev = []
data_train_temp = data.sample(frac=0.9)
data_test = data.drop(data_train_temp.index)
data_train = data_train_temp.sample(frac=8 / 9)
data_dev = data_train_temp.drop(data_train.index)

"""
jieba分词
"""


def jieba_data(temp_data):
    jieba.load_userdict('./data/userdict1.txt')
    data_cut = temp_data.apply(lambda x: jieba.lcut(x))
    # 去除停用词 csv 默认 ,作为分隔符 用sep取一个数据里不存在的字符作为分隔符保障顺利读取
    stop_words = pd.read_csv('data/stopword.txt', sep='hhhh', encoding='GB18030', engine='python')
    # pd转列表拼接  iloc[:,0] 取第0列
    stop_words = list(stop_words.iloc[:, 0]) + [' ', '...', '', '  ', '→', '-', '：', ' ●', '\t', '\n']
    data_after_stop = data_cut.apply(lambda x: [i.strip() for i in x if i not in stop_words])
    # data_after_stop = data_after_stop.apply(lambda x: [i.strip() for i in x if i not in list(stop_words2.iloc[:, 0])])
    # 去除空格
    data_after_stop = data_after_stop.apply(lambda x: [i for i in x if i != ''])
    # 空格分割字符
    data_str = data_after_stop.apply(lambda x: ' '.join(x))
    return data_str


data_train_jieba = jieba_data(data_train['留言主题'])
data_test_jieba = jieba_data(data_test['留言主题'])
data_dev_jieba = jieba_data(data_dev['留言主题'])
for i in data_train_jieba:
    train.append(str(i))
for i in data_train['一级标签']:
    y_train.append(classification.index(i))
for i in data_test_jieba:
    test.append(str(i))
for i in data_test['一级标签']:
    y_test.append(classification.index(i))
for i in data_dev_jieba:
    dev.append(str(i))
for i in data_dev['一级标签']:
    y_dev.append(classification.index(i))

# -----------------------------------------------------------------------#
# for i in data_train['留言主题']:
#     train.append(
#         str(i).strip().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\u3000',
#                                                                                                       '').replace(
#             '\xa0', ''))
# for i in data_train['一级标签']:
#     y_train.append(classification.index(i))
# for i in data_test['留言主题']:
#     test.append(
#         str(i).strip().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\u3000',
#                                                                                                       '').replace(
#             '\xa0', ''))
# for i in data_test['一级标签']:
#     y_test.append(classification.index(i))
#
# for i in data_dev['留言主题']:
#     dev.append(
#         str(i).strip().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\u3000',
#                                                                                                       '').replace(
#             '\xa0', ''))
# for i in data_dev['一级标签']:
#     y_dev.append(classification.index(i))

# --------------------------------------------------------------
# def generate_data(data_set):
#     temp_data = []
#     temp_y = []
#     for index in data_set['留言详情']:
#         temp_data.append(
#             str(index).strip().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\u3000',
#                                                                                                               '').replace(
#                 '\xa0', ''))
#     for index in data_set['一级标签']:
#         temp_y.append(classification.index(index))
#     return temp_data , temp_y


path = './tempdata/'
# path = '/home/asimov/PycharmProjects/Chinese-Text-Classification-Pytorch/THUCNews/data/'
# path='/home/asimov/PycharmProjects/Bert-Chinese-Text-Classification-Pytorch/THUCNews/data/'
name = "theme_jieba"
with open(path + 'train_' + name + '.txt', 'w') as f:
    for i in range(len(y_train)):
        f.write(str(train[i]))
        f.write('\t')
        f.write(str(y_train[i]))
        f.write('\n')
with open(path + 'test_' + name + '.txt', 'w') as f:
    for i in range(len(y_test)):
        f.write(str(test[i]))
        f.write('\t')
        f.write(str(y_test[i]))
        f.write('\n')
with open(path + 'dev_' + name + '.txt', 'w') as f:
    for i in range(len(y_dev)):
        f.write(str(dev[i]))
        f.write('\t')
        f.write(str(y_dev[i]))
        f.write('\n')
#
# with open('./test2.txt', 'r', encoding='UTF-8') as f:
#     for line in tqdm(f):
#         # print(line)
#         lin = line.strip()
#         if not lin:
#             continue
#         content, label = lin.split('\t')
#         # print(line)
lens = []
for i in range(y_train.__len__()):
    lens.append(len(train[i]))
shapes = pd.DataFrame(lens).describe()
