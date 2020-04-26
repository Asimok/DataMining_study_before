import pandas as pd

"""
训练集处理
"""
classification = ['城乡建设', '环境保护', '交通运输', '教育文体', '劳动和社会保障', '商贸旅游', '卫生计生']
data = pd.read_excel('/home/asimov/PycharmProjects/DataMining/C_data/附件2.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('/home/asimov/PycharmProjects/DataMining/C_data/附件1.xlsx', sheet_name='Sheet1')
test = []
y_test = []
train = []
y_train = []
dev = []
y_dev = []
data_temp = data.sample(frac=0.4)
data_train = data.drop(data_temp.index)
data_test = data_temp.sample(frac=0.5)
data_dev = data_temp.drop(data_test.index)

for i in data_train['留言详情']:
    train.append(
        str(i).strip().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\u3000',
                                                                                                      '').replace('*',
                                                                                                                  '').replace(
            '\xa0', ''))
for i in data_train['一级标签']:
    y_train.append(i)
for i in data_test['留言详情']:
    test.append(
        str(i).strip().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\u3000',
                                                                                                      '').replace('*',
                                                                                                                  '').replace(
            '\xa0', ''))
for i in data_test['一级标签']:
    y_test.append(i)

for i in data_dev['留言详情']:
    dev.append(
        str(i).strip().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\u3000',
                                                                                                      '').replace('*',
                                                                                                                  '').replace(
            '\xa0', ''))
for i in data_dev['一级标签']:
    y_dev.append(i)

# -----------------------------------------------------------------------#
# for i in data_train['留言主题']:
#     train.append(
#         str(i).strip().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\u3000',
#                                                                                                       '').replace('*',
#                                                                                                                   '').replace(
#             '\xa0', ''))
# for i in data_train['一级标签']:
#     y_train.append(classification.index(i))
# for i in data_test['留言主题']:
#     test.append(
#         str(i).strip().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\u3000',
#                                                                                                       '').replace('*',
#                                                                                                                   '').replace(
#             '\xa0', ''))
# for i in data_test['一级标签']:
#     y_test.append(classification.index(i))
#
# for i in data_dev['留言主题']:
#     dev.append(
#         str(i).strip().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\u3000',
#                                                                                                       '').replace('*',
#                                                                                                                   '').replace(
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


with open('/home/asimov/PycharmProjects/DataMining/C_data/processed/cnews.train.txt', 'w') as f:
    for i in range(len(y_train)):
        f.write(str(y_train[i]))
        f.write('\t')
        f.write(str(train[i]))
        f.write('\n')
with open('/home/asimov/PycharmProjects/DataMining/C_data/processed/cnews.test.txt', 'w') as f:
    for i in range(len(y_test)):
        f.write(str(y_test[i]))
        f.write('\t')
        f.write(str(test[i]))
        f.write('\n')
with open('/home/asimov/PycharmProjects/DataMining/C_data/processed/cnews.val.txt', 'w') as f:
    for i in range(len(y_dev)):
        f.write(str(y_dev[i]))
        f.write('\t')
        f.write(str(dev[i]))
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
max = 0
for i in range(train.__len__()):
    lens.append(len(train[i]))
    if len(train[i]) > max:
        max = len(train[i])
        print(max, '  ', i)
shapes = pd.DataFrame(lens).describe()
