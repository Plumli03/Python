import numpy as np
import pandas as pd

df = pd.read_csv('新竹市重要遊憩據點遊客人次統計.csv', encoding='Big5', sep='\t')
df = df.drop(columns=['Countycode','YYYMM'])
df = df.astype('int32')
df['民國年月'] = df['民國年月'].astype('str')
df['年'] =  df['民國年月'].str[:3]
df = df.set_index('民國年月')

import matplotlib as mpl
mpl.rc('font', family='Microsoft JhengHei')
Accent = mpl.colormaps['Accent']
new_Accent = [Accent(n) for n in range(8)]  # 選好了八個顏色

df_g = df.groupby("年").sum() # 各年總人數
據點 = df_g.columns
據點顏色配對字典 = {}
for n,item in enumerate(據點) :
    據點顏色配對字典[item]=new_Accent[n]
# print(據點顏色配對字典)

s1 = df.sum(numeric_only=True).sort_values(ascending=False) #108年-112年五年總人數 ( 有排序 )
#print(s1)
#print(s1.index[0])
new_Accent1 = [  據點顏色配對字典[s1.index[n]] for n in range(8) ]  # 利用據點名字拿到顏色，產生一個調整過順序的調色盤
#print(new_Accent1)

據點 = [item[:-2] for item in 據點]  # 簡化據點的名字
據點索引 = [n for n in range(len(據點))]

import matplotlib.pyplot as plt

fig, ax = plt.subplots(nrows=3, ncols=2, constrained_layout=True, figsize=(21, 18))
fig.suptitle('108年-112年 新竹市重要遊憩據點遊客人數分布統計',color='red',fontsize=18)

#  小圖一
據點1 = s1.index
據點1 = [item[:-2] for item in 據點1]
據點索引1 = [n for n in range(len(據點1))]
人數1 = s1
ax[0,0].bar(據點1 , 人數1, color=new_Accent1)
ax[0,0].set_xlabel('據點',color='red',fontsize=12)
ax[0,0].set_ylabel('人數(百萬)',color='red',fontsize=12)
ax[0,0].set_xticks(據點索引1,據點1,color='red',rotation=20)
ax[0,0].set_yticks([n for n in range(0,20000001,5000000)],
                   [str(n) for n in range(0,21,5) ],color='red')
ax[0,0].set_title('近5年總人數統計', loc='left')

#  小圖二 108年
人數 = df_g.loc['108']
ax[0,1].bar(據點 , 人數, color=new_Accent)
ax[0,1].set_xlabel('據點',color='red',fontsize=12)
ax[0,1].set_ylabel('人數',color='red',fontsize=12)
ax[0,1].set_xticks(據點索引,據點,color='red',rotation=20)
ax[0,1].set_yticks([n for n in range(0,5000001,1000000)],
                   [str(n) for n in range(0,51,10) ],color='red')
ax[0,1].set_title('108年總人數統計', loc='left')

#  小圖三 109年
人數 = df_g.loc['109']
ax[1,0].bar(據點 , 人數, color=new_Accent)
ax[1,0].set_xlabel('據點',color='red',fontsize=12)
ax[1,0].set_ylabel('人數',color='red',fontsize=12)
ax[1,0].set_xticks(據點索引,據點,color='red',rotation=20)
ax[1,0].set_yticks([n for n in range(0,5000001,1000000)],
                   [str(n) for n in range(0,51,10) ],color='red')
ax[1,0].set_title('109年總人數統計', loc='left')

#  小圖四 110年
人數 = df_g.loc['110']
ax[1,1].bar(據點 , 人數, color=new_Accent)
ax[1,1].set_xlabel('據點',color='red',fontsize=12)
ax[1,1].set_ylabel('人數',color='red',fontsize=12)
ax[1,1].set_xticks(據點索引,據點,color='red',rotation=20)
ax[1,1].set_yticks([n for n in range(0,5000001,1000000)],
                   [str(n) for n in range(0,51,10) ],color='red')
ax[1,1].set_title('110年總人數統計', loc='left')

#  小圖五 111年
人數 = df_g.loc['111']
ax[2,0].bar(據點 , 人數, color=new_Accent)
ax[2,0].set_xlabel('據點',color='red',fontsize=12)
ax[2,0].set_ylabel('人數',color='red',fontsize=12)
ax[2,0].set_xticks(據點索引,據點,color='red',rotation=20)
ax[2,0].set_yticks([n for n in range(0,5000001,1000000)],
                   [str(n) for n in range(0,51,10) ],color='red')
ax[2,0].set_title('111年總人數統計', loc='left')

#  小圖六 112年
人數 = df_g.loc['112']
ax[2,1].bar(據點 , 人數, color=new_Accent)
ax[2,1].set_xlabel('據點',color='red',fontsize=12)
ax[2,1].set_ylabel('人數',color='red',fontsize=12)
ax[2,1].set_xticks(據點索引,據點,color='red',rotation=20)
ax[2,1].set_yticks([n for n in range(0,5000001,1000000)],
                   [str(n) for n in range(0,51,10) ],color='red')
ax[2,1].set_title('112年總人數統計', loc='left')

plt.show()
plt.savefig("Customed Plot.pdf", dpi=300, bbox_inches="tight")
