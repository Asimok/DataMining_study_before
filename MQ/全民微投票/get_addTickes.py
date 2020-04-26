import re

import pandas as pd

data = pd.read_excel('./data/加票汇总.xlsx')
name = data['选手']
name = name.apply(lambda x: re.sub('\xa0', ' ', x))
addTickes = data['票数']
data_new = pd.concat([name, addTickes], axis=1)

data_new2 = data_new.groupby(by='选手').sum()
data_new2.to_excel('data.xlsx')
data2 = pd.read_excel('data.xlsx')
data_sort = data2.sort_values(by='票数', ascending=False)
# data_sort.to_excel('data.xlsx')

total = data_sort.set_index('选手')['票数'].to_dict()

rank = pd.read_excel('./data/全民微投票-“创建”杯创意健身微视频大赛-2020-04-09.xls')
rank_name = rank['选手编号'].apply(lambda x: str(x) + "号") + " " + rank['姓名']
rank_name = rank_name.apply(lambda x: re.sub('\xa0', ' ', x))
rank_tickets = rank['票数']
rank_add = []
for key in rank_name:
    val = total.get(key)
    if val == None:
        val = 0
    rank_add.append(val)

rank_pure = []
for i in range(rank_tickets.size):
    rank_pure.append(int(rank_tickets[i] - int(rank_add[i])))

data_all = pd.DataFrame({'姓名': rank_name, "总票数": rank_tickets, "购买票数": rank_add, "实际票数": rank_pure},columns=['姓名','总票数','购买票数','实际票数'])
data_all.to_excel('投票结果.xlsx')
