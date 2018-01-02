#coding:UTF-8
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
def date_total(i):
    date1 = df.ix[i, 1].split('.')
    date1 = datetime.date(int(date1[0]), int(date1[1]), int(date1[2]))
    date2 = df.ix[i, 2].split('.')
    date2 = datetime.date(int(date2[0]), int(date2[1]), int(date2[2]))
    day = date2 - date1
    day=str(day)
    day=day.split('d')[0].strip()
    day=long(day)
    week_count=day/7
    week_count=round(week_count)

    return week_count

film_name=[]
film_averagebox=[]
df=pd.read_csv("film_log3.csv",delimiter=';',names=['电影名称','上映日期','下映日期','制作公司','导演','演员','剧情分类','票房','上映城市'])
for i in xrange(len(df)):
    if((df.ix[i,0]=='《冲上云霄》'and df.ix[i,-1]=='北京') or (df.ix[i,0]=='《一念天堂》'and df.ix[i,-1]=='沈阳') or (df.ix[i,0]=='《百团大战》'and df.ix[i,-1]=='成都')):
        week_count=date_total(i)
        box = df.ix[i, -2]
        box = float(box.split('）')[-1].strip())
        average=box/week_count
        average='%.6f'%average
        film_name.append(df.ix[i,0])
        film_averagebox.append(average)
# for i in xrange(len(film_name)):
#     print film_name[i]
#     print film_averagebox[i]
x=np.arange(3)+1
plt.bar(x,film_averagebox)
plt.xticks(x,['A','B','C'])
plt.show()
a=np.array(film_averagebox)
a.tofile('ans0302.dat',sep=',')