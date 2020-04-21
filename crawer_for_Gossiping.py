#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[1]:


import requests
import numpy as np
from bs4 import BeautifulSoup
import itertools
import warnings
warnings.filterwarnings("ignore")
import sys
sys.setrecursionlimit(90000000) 
from tqdm import tnrange, tqdm_notebook, tqdm
import pandas as pd


# In[2]:


def URL_find_block(URL_):
    while(True):
        try: 
            # 開始request
            payload = {
                "from": "/bbs/Gossiping/index.html",
                "yes": "yes"
            }
            rs = requests.session()
            res = rs.post("https://www.ptt.cc/ask/over18", verify = False, data = payload)
            res = rs.get(URL_, verify = False, headers={'Connection':'close'}) 

            # 若存取成功則以 soup紀錄內容並找出class 為 r-ent的區段並回傳
            soup = BeautifulSoup(res.text)
            return(soup.select(".r-ent"))
            break
        except:
            # 若錯誤則 print url
            print("error happend: %s" % (URL_))


# In[3]:


def block_get_title_data(block_):
    buf_title = "block_get_title_data---error---"
    buf_date = "block_get_title_data---error---"
    try:
        buf_title = block_.select(".title")[0].select("a")[0].text
        buf_date = block_.select(".date")[0].text
    except:
        print("error in block_get_title_data")
        #print(block_)
        
    return( (buf_title, buf_date) )


# In[4]:


def output_data(buf_):
    df = pd.DataFrame(buf_)
    df.columns = ["title", "date"]
    # delete some data
    df = df[df['title'] != "block_get_title_data---error---" ]
    name = "Gossip_title_%d_to_%d.csv" % (START, END)
    df.to_csv(name, index = False, encoding= 'UTF-8')


# In[5]:


if __name__ == '__main__':
    START, END = int(sys.argv[1]), int(sys.argv[2])
    #START, END = 39045, 39048
    print("start get data from page %d to %d" % (START, END)) 
    list_URL = ["https://www.ptt.cc/bbs/Gossiping/index" + str(i) + ".html"
                for i in np.arange(START, END+1)]

    print("start to get all the block")
    buf = [ URL_find_block(i) for i in tqdm(list_URL)]
    list_block = list(itertools.chain(*buf))

    print("start to get title and data from block")
    buf = [ block_get_title_data(i) for i in tqdm(list_block)]

    try:
        output_data(buf)
        print("success to create file Gossip_title_%d_to_%d.csv" % (START, END) )
    except:
        print("fail to create file " )


# In[ ]:




