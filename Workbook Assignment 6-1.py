#!/usr/bin/env python
# coding: utf-8

# In[1]:


cd


# In[2]:


import pandas as pd
Location = "Desktop/ISM 4402/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[5]:


df = df.sort_values(by=['fname', 'lname', 'age', 'grade'],
                    ascending=[True, True, True, True])
df.head()


# In[ ]:




