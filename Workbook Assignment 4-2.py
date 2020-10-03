#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "Desktop/ISM 4402/datasets/gradedata.csv"
df = pd.read_csv(Location)


# In[2]:


df.head()


# In[3]:


import numpy as np


# In[4]:


df['timemgmt'] = np.where((df['exercise']>3) & (df['hours']>17),'busy', 'not busy')
df.tail(10)


# In[ ]:




