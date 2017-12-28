#coding:UTF-8
import re
import pandas as pd
input_open=open("spider.log")
film_name=[]
date_start=[]
date_end=[]
box_of_return=[]
df_topic=['电影名称','上映日期','结束放映日期','票房收入']
try:
    for line in input_open:
        # print line
        str=re.findall(r'.+,http://www\.movie\.com/bor/12386／,.+;.+;.+;.+;.+;.+;.+;.+;.+;|.+,http://www\.movie\.com/bor/,.+;.+;.+;.+;.+;.+;.+;.+;.+;',line)
        if(len(str)!=0):
            for i in str:
                filmName=i.split(";")[0]
                filmName=filmName.split(",")[2]
                film_name.append(filmName)
                dateStart=i.split(";")[1]
                date_start.append(dateStart)
                dateEnd=i.split(";")[2]
                date_end.append(dateEnd)
                box=i.split(";")[-3]
                box=box.split("）")[-1].strip()
                box_of_return.append(box)
                df=pd.DataFrame({'电影名称':film_name,'上映日期':date_start,'结束放映日期':date_end,'票房收入':box_of_return})

    print df
    df.to_csv("ans0201.csv")
    # for i in film_name:
    #     print i
finally:
    input_open.close()