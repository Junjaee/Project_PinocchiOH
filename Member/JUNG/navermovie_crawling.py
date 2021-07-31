#!/usr/bin/env python
# coding: utf-8

# In[1]:


from wordcloud import WordCloud 
import matplotlib.pyplot as plt 
import nltk 
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib as mpl #->한글 깨지는 거때매 추가하는거
import matplotlib.font_manager as fm  #-> 폰트 지정가능

import seaborn as sns


# 한글 설정
import matplotlib as mpl
mpl.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False 

import time
from tqdm import tqdm_notebook


# In[109]:


import requests
from urllib import parse
from bs4 import BeautifulSoup
base_url = 'https://movie.naver.com/movie/point/af/list.nhn?&page={}'
url = base_url.format(1)
res=requests.get(url)

if res.status_code == 200:
    soup = BeautifulSoup(res.text)
    
    tds = soup.select('table.list_netizen > tbody > tr')
    print(len(tds))
    for td in tds:
        movie_title = td.select_one('td.title > a.movie').text.strip()
        score = td.select_one('td.title > div.list_netizen_score > em').text.strip()
        comment = td.select_one('td.title > br').next_sibling.strip() #textnode 인 경우 text 로 조회할 필요 없다
        user_id = td.select_one('td.num > a.author').text.strip()
        
        
    print(movie_title, score, comment, user_id, sep=' :: ')
        
    print('-------------------------------------------------')


# In[110]:


import random
random.uniform(0.2, 1.2) #이 사이의 실수를 동일한 확률로 나오게 한다.


# In[115]:


import requests
import time
import random
from bs4 import BeautifulSoup


base_url = 'https://movie.naver.com/movie/point/af/list.nhn?&page={}'
#결과 저장할 리스트
comment_list = []
#총 1~1000page 까지 있으니, (1,1001)로 range 잡고 하면됨
for page in range(1, 501):
    url = base_url.format(page)
    res=requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'lxml')
        tds = soup.select('table.list_netizen > tbody > tr')
        for td in tds:
            movie_title = td.select_one('td.title > a.movie').text.strip()
            score = td.select_one('td.title > div.list_netizen_score > em').text.strip()
            comment = td.select_one('td.title > br').next_sibling.strip() #textnode 인 경우 text 로 조회할 필요 없다
            user_id = td.select_one('td.num > a.author').text.strip()
            # 리스트에 저장
            comment_list.append((movie_title, user_id, score, comment))
        interval = round(random.uniform(0.2, 1.2), 2)
        time.sleep(interval)
print('종료') 


# In[116]:


import pandas as pd
df = pd.DataFrame(comment_list, 
                  columns=['영화제목','아이디', '평점','댓글'])
df.to_csv('naver_movie_review_data_part_1.csv', encoding='utf-8', index=False)


# In[117]:


pd.read_csv('naver_movie_review_data_part_1.csv')


# In[ ]:





# In[ ]:




