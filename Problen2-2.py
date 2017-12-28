#coding:UTF-8
import re
import pandas as pd
import os
import numpy as np
input_url=open("movie_review.htm")
film_name=[]
film_score=[]
try:
    url_read=input_url.read()
    # print url_read
    str_filmName=re.findall(r'<a href="https://movie\.douban\.com/subject/\d*/\?from=playing_poster" class="ticket-btn" target="_blank" title=".*" data-psource="title">|<a href="https://movie\.douban\.com/subject/\d+/\?from=playing_poster" class="" target="_blank" title=".*" data-psource="title">', url_read)
    for i in str_filmName:
        # print i
        filmName=i.split("title=\"")[-1]
        filmName=filmName.split("\"")[0]
        film_name.append(filmName)
    score_Start=url_read.find('<ul class="lists">')
    if score_Start==-1:
        print"score_Start not found"
        os._exit()
    artcle=url_read[score_Start:-1]
    score_End=artcle.find('<div id="upcoming">')#搜索会返回关键字前面的位置
    if score_End==-1:
        print"score_End not found"
        os._exit()
    artcle=artcle[:score_End]
    # print artcle
    str_Score=re.findall(r'<span class="subject-rate">.*</span>|<span class="text-tip">暂无评分</span>',artcle)
    for i in str_Score:
        score=i.split('">')[-1]
        score=score.split('<')[0].strip(" ").replace(' ','')
        if(score=='暂无评分'):
            score=0
        float(score)
        film_score.append(score)
    array_Score=np.array(film_score)
    df=pd.DataFrame({'电影名称':film_name,'评分':array_Score},dtype=float)
    print df
    print df.describe()


finally:
    input_url.close()