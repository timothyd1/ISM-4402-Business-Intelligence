#!/usr/bin/env python
# coding: utf-8

# In[1]:


cd C:/Users/Timothy Davis/Desktop/ISM 4402


# In[2]:


import pandas as pd


# In[3]:


import numpy as np


# In[4]:


import glob


# In[5]:


all_data = pd.DataFrame()


# In[9]:


for f in glob.glob("weekly_call_data/weekdata*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)


# In[12]:


all_data.describe()


# In[ ]:




