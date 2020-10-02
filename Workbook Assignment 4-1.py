#!/usr/bin/env python
# coding: utf-8

# In[1]:


cd


# In[2]:


import pandas as pd
Location = "Desktop/ISM 4402/datasets/gradedata.csv"
df = pd.read_csv(Location)


# In[7]:


df.head()


# In[8]:


bins = [0, 79.9, 100]
group_names = ['Fail', 'Pass']


# In[9]:


df['passorfail'] = pd.cut(df['grade'], bins,
                           labels=group_names)
df


# In[10]:


pd.value_counts(df['passorfail'])


# In[ ]:




