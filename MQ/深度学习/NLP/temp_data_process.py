import pandas as pd

"""
训练集处理
"""
classification = ['城乡建设', '环境保护', '交通运输', '教育文体', '劳动和社会保障', '商贸旅游', '卫生计生']
data_train = pd.read_excel('./data/训练集.xlsx', sheet_name='Sheet1')
text_tr = []
y_tr = []

for i in data_train['留言详情']:
    text_tr.append(
        str(i).strip().replace(' ', '').replace('\n', '').replace('\t', '').replace('\u3000', '').replace('\xa0', ''))

for i in data_train['一级分类']:
    y_tr.append(classification.index(i))
data = pd.DataFrame({'label': y_tr, 'text': text_tr}, columns=['label', 'text'])
data.to_csv('/home/asimov/PycharmProjects/DataMining/MQ/Bert/data/train.csv',index=None)

file_path = '/home/asimov/PycharmProjects/DataMining/MQ/Bert/data/train.csv'


def read_txt_file(file_path):
    read_data = pd.read_csv(file_path,index_col=None)
    labels, texts = [], []
    labels=read_data['label']
    texts=read_data[1]

    return labels, texts
