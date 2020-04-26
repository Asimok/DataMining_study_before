import pandas as pd
import re
df = pd.read_excel(r"附件2.xlsx", usecols=[2, 4], names=None)
df_li = df.values.tolist()
# for i in df_li:
#     print(i)


# print(test.strip())

# 提取特有地名到用户自建词表
ress = []
pattern = re.compile(r'[A-Z]{1}[0-9]*[\u7701|\u5e02|\u533a|\u53bf|\u4e61|\u6751|\u9547]{1}')
for s_li in df_li:
    res_top = pattern.findall(s_li[0])
    res_con = pattern.findall(s_li[1])
    res_top = res_top+res_con
    ress = ress + res_top
ress = list(set(ress))
print(ress)
with open('userdict1.txt','w') as f:
    for user_want in ress:
        print(user_want)
        f.writelines(user_want + "\n")
# user_init = open(r"userdict1.txt",'a',encoding='utf-8')
