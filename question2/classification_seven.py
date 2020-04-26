import jieba.analyse
import jieba.posseg as psg
import pandas as pd

classification = ['城乡建设', '环境保护', '交通运输', '教育文体', '劳动和社会保障', '商贸旅游', '卫生计生']
data = pd.read_excel('/home/asimov/PycharmProjects/DataMining/question2/data/附件3_labels.xlsx', sheet_name='Sheet1')

cxjs_data = data.loc[data['预测一级标签'] == classification[0]]
hjbh_data = data.loc[data['预测一级标签'] == classification[1]]
jtys_data = data.loc[data['预测一级标签'] == classification[2]]
jywt_data = data.loc[data['预测一级标签'] == classification[3]]
ldhshbz_data = data.loc[data['预测一级标签'] == classification[4]]
smly_data = data.loc[data['预测一级标签'] == classification[5]]
wsjs_data = data.loc[data['预测一级标签'] == classification[6]]

cxjs_data.to_excel('/home/asimov/PycharmProjects/DataMining/question2/classifications_seven/cxjs_data.xls')
hjbh_data.to_excel('/home/asimov/PycharmProjects/DataMining/question2/classifications_seven/hjbh_data.xls')
jtys_data.to_excel('/home/asimov/PycharmProjects/DataMining/question2/classifications_seven/jtys_data.xls')
jywt_data.to_excel('/home/asimov/PycharmProjects/DataMining/question2/classifications_seven/jywt_data.xls')
ldhshbz_data.to_excel('/home/asimov/PycharmProjects/DataMining/question2/classifications_seven/ldhshbz_data.xls')
smly_data.to_excel('/home/asimov/PycharmProjects/DataMining/question2/classifications_seven/smly_data.xls')
wsjs_data.to_excel('/home/asimov/PycharmProjects/DataMining/question2/classifications_seven/wsjs_data.xls')
"""
l:习用语 nr:人名 nz:其他专名
"""
jieba.load_userdict('./data/new_places.txt')
# str = cxjs_data['留言主题'][2]
str = '反映M9县春华镇金鼎村水泥路、自来水到户的问题'
print(str)
keywords = " ".join(jieba.analyse.extract_tags(sentence=str, topK=10, withWeight=False, allowPOS=(['n', 'ns','l'])))
print(keywords)
keywords = jieba.analyse.extract_tags(sentence=str, topK=5, withWeight=True, allowPOS=(['n', 'v']))
print(keywords)

print('分词及词性：')
result = psg.cut(str)
print(result)
print([(x.word, x.flag) for x in result])
