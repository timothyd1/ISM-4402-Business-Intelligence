#!/usr/bin/env python
# coding: utf-8

# In[1]:


cd C:/Users/Timothy Davis/Desktop/ISM 4402


# In[2]:


import pandas as pd


# In[3]:


from sqlalchemy import create_engine


# In[4]:


db_file = r'datasets/salesdata.db'


# In[5]:


engine = create_engine(r"sqlite:///{}".format(db_file))


# In[17]:


sql = 'SELECT * from scores'


# In[18]:


sales_data_df = pd.read_sql(sql, engine)


# In[19]:


sales_data_df


# In[ ]:




