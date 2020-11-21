#!/usr/bin/env python
# coding: utf-8

# In[21]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
Location = "Desktop/ISM 4402/datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


df["Cars Sold"].mean()


# In[4]:


df["Cars Sold"].max()


# In[5]:


df["Cars Sold"].min()


# In[7]:


df.groupby("Gender")["Cars Sold"].mean()


# In[26]:


hours_worked=df[df["Cars Sold"]>3]["Hours Worked"]
avg_hours_worked=np.mean(hours_worked)
print(avg_hours_worked)


# In[11]:


df["Years Experience"].mean()


# In[25]:


experience=df[df["Cars Sold"]>3]["Years Experience"]
avg_experience=np.mean(experience)
print(avg_experience)


# In[15]:


df.groupby("SalesTraining")["Cars Sold"].mean()


# In[59]:


df.hist(column="Cars Sold", by="SalesTraining")


# In[55]:


pd.pivot_table(df,
 index=['Cars Sold'],
 aggfunc='mean',
 values=['Hours Worked'])


# In[57]:


print('The best indicator is the Average hours worked per month because it gives the best indication of how many cars a sales person will sell.')


# In[ ]:




