#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = "Desktop/ISM 4402/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


df['sex_female']=df.gender.map({'female':1,'male':0})
df.head()


# In[4]:


import statsmodels.formula.api as sm
result = sm.ols(
    formula='grade ~ age + exercise + hours + sex_female',
    data=df).fit()
result.summary()


# In[5]:


import statsmodels.formula.api as sm
result = sm.ols(
    formula='grade ~ exercise + hours + sex_female',
    data=df).fit()
result.summary()


# In[ ]:




