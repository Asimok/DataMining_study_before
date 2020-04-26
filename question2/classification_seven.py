import pandas as pd

classification = ['城乡建设', '环境保护', '交通运输', '教育文体', '劳动和社会保障', '商贸旅游', '卫生计生']
data = pd.read_excel('/home/asimov/PycharmProjects/DataMining/question2/data/附件3_labels.xlsx', sheet_name='Sheet1')

cxjs_data = []
hjbh_data = []
jtys_data = []
jywt_data = []
ldhshbz_data = []
smly_data = []
wsjs_data = []

