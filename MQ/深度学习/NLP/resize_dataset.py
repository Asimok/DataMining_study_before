import random

import pandas as pd

classification = ['城乡建设', '环境保护', '交通运输', '教育文体', '劳动和社会保障', '商贸旅游', '卫生计生']
data = pd.read_excel('/home/asimov/PycharmProjects/DataMining/C_data/附件2.xlsx', sheet_name='Sheet1')
classification_num = list(data['一级标签'].value_counts())
test = []
y_test = []
train = []
y_train = []
dev = []
y_dev = []


def get_temp_val(data_train, data_test, data_dev):
    for index in data_train['留言详情']:
        train.append(
            str(index).strip().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\u3000',
                                                                                                              '').replace(
                '*',
                '').replace(
                '\xa0', ''))
    for index in data_train['一级标签']:
        y_train.append(classification.index(index))
    for index in data_test['留言详情']:
        test.append(
            str(index).strip().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\u3000',
                                                                                                              '').replace(
                '*',
                '').replace(
                '\xa0', ''))
    for index in data_test['一级标签']:
        y_test.append(classification.index(index))

    for index in data_dev['留言详情']:
        dev.append(
            str(index).strip().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\u3000',
                                                                                                              '').replace(
                '*',
                '').replace(
                '\xa0', ''))
    for index in data_dev['一级标签']:
        y_dev.append(classification.index(index))


# 比例 8
for i in range(7):
    get_temp_data = data.loc[data['一级标签'] == classification[i]]
    temp_data = get_temp_data.sample(frac=0.35)
    temp_train = get_temp_data.drop(temp_data.index)
    temp_test = temp_data.sample(frac=0.2)
    temp_dev = temp_data.drop(temp_test.index)
    get_temp_val(temp_train, temp_test, temp_dev)

# 打乱顺序
end_data_train = pd.DataFrame({'data': train, 'label': y_train})
end_data_train = end_data_train.sample(frac=1).reset_index(drop=True)
train_end = end_data_train['data']
y_train_end = end_data_train['label']

end_data_test = pd.DataFrame({'data': test, 'label': y_test})
end_data_test = end_data_test.sample(frac=1).reset_index(drop=True)
test_end = end_data_test['data']
y_test_end = end_data_test['label']

end_data_dev = pd.DataFrame({'data': dev, 'label': y_dev})
end_data_dev = end_data_dev.sample(frac=1).reset_index(drop=True)
dev_end = end_data_dev['data']
y_dev_end = end_data_dev['label']

path = '/home/asimov/PycharmProjects/Chinese-Text-Classification-Pytorch/THUCNews/data/'
# path='/home/asimov/PycharmProjects/DataMining/C_data/processed/'
name = "detail"
with open(path + 'train_' + name + '.txt', 'w') as f:
    for i in range(len(y_train_end)):
        f.write(str(train_end[i]))
        f.write('\t')
        f.write(str(y_train_end[i]))
        f.write('\n')
with open(path + 'test_' + name + '.txt', 'w') as f:
    for i in range(len(y_test_end)):
        f.write(str(test_end[i]))
        f.write('\t')
        f.write(str(y_test_end[i]))
        f.write('\n')
with open(path + 'dev_' + name + '.txt', 'w') as f:
    for i in range(len(y_dev_end)):
        f.write(str(dev_end[i]))
        f.write('\t')
        f.write(str(y_dev_end[i]))
        f.write('\n')

lens = []
max1 = 0
min1 = 5
nums = 0
for i in range(train_end.__len__()):
    lens.append(len(train_end[i]))
    if len(train_end[i]) > max1:
        max1 = len(train_end[i])
        print(max1, '  ', i)
    if len(train_end[i]) < min1:
        nums += 1
print('nums:', nums)
shapes = pd.DataFrame(lens).describe()
