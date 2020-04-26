import pandas as pd

from MQ.黑龙江空气预测.tool import set_AQI

data = pd.read_excel('./data/shuju.xlsx')
AQI = list(data['AQI'])
quality = list(data['质量等级'])
for i in range(AQI.__len__()):
    quality[i] = set_AQI(AQI[i])
quality = pd.DataFrame({'质量等级': quality})
data['质量等级'] = quality

# 拆分年月日
# 2013-12-02 0:00:00
DATE = list(data['日期'])
DATE2 = list(data['日期'])
YEAR = []
MONTH = []
DAY = []

for i in range(len(DATE)):
    year, month, day = str(DATE[i]).split(' ')[0].split('-')
    YEAR.append(int(year))
    MONTH.append(int(month))
    DAY.append(int(day))
newDate = pd.DataFrame({'年': YEAR, '月': MONTH, '日': DAY})
data.insert(0, "月", MONTH)
data.insert(0, "年", YEAR)
data['日期'] = DAY
data.rename(columns={'日期': '日'}, inplace=True)
# data.to_excel('./data/new.xlsx')

ansDATE=[]
for i in range(len(DATE2)):
    year, month, day = str(DATE[i]).split(' ')[0].split('-')
    year=str(year)[-2:]
    ansDATE.append(str(day)+'/'+month+'/'+year)
loc=[]
for j in range(len(ansDATE)):
    loc.append('黑龙江')
val= pd.DataFrame({'地点':loc,'AQI': AQI, '日期':ansDATE},columns=['地点','AQI','日期'])
val.to_csv('./data/test.csv',header=None,index=None)
