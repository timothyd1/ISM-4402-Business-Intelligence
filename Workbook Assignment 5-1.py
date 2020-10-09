#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


import numpy as np


# In[5]:


Location = "Desktop/ISM 4402/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.tail()


# In[6]:


df.take(np.random.permutation(len(df))[:500])


# In[ ]:




