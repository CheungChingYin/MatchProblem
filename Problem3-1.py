#coding:UTF-8
import pandas as pd
import time
import datetime
import numpy as np
count=0
total=0.0
def date_total(i):
    date1 = df.ix[i, 1].split('.')
    date1 = datetime.date(int(date1[0]), int(date1[1]), int(date1[2]))
    date2 = df.ix[i, 2].split('.')
    date2 = datetime.date(int(date2[0]), int(date2[1]), int(date2[2]))
    day = date2 - date1
    day=str(day)
    day=day.split('d')[0].strip()
    day=long(day)
    return day

df=pd.read_csv("film_log3.csv",delimiter=';',names=['电影名称','上映日期','下映日期','制作公司','导演','演员','剧情分类','票房','上映城市'])
for i in xrange(len(df)):
    if(df.ix[i,0]=='《冲上云霄》'and df.ix[i,-1]=='北京'):
        count+=1
        box = df.ix[i, -2]
        box = box.split('）')[-1].strip()
        total += float(box)
        day=date_total(i)
average=total/count
average='%.6f'%average
a=np.array([day,average])
a.tofile('ans0301.dat',sep=',')

print average




