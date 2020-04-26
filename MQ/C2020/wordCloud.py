import matplotlib.pyplot as plt
from wordcloud import WordCloud

from MQ.C2020.data_process import data_process

data_str_train, data_after_stop_train, labels_train = data_process(file='./data/训练集.xlsx')
# 统计词频
dic = {}
for i in data_after_stop_train:
    for j in i:
        if j not in dic.keys():
            dic[j] = 1
        else:
            dic[j] += 1

mask = plt.imread('./data/duihuakuan.jpg')
wc = WordCloud(font_path='/usr/share/fonts/opentype/noto/NotoSerifCJK-Medium.ttc', mask=mask, background_color='white')
wc.fit_words(dic)
plt.imshow(wc)
plt.imsave('word.png',wc)
plt.axis('off')
plt.show()
