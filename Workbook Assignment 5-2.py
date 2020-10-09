#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
StudentInfo = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data=StudentInfo,
                  columns=['Names','Grades','BS Degrees','MS Degrees','PHD Degrees'])
df


# In[3]:


df['Grades'].count()


# In[4]:


df['Grades'].mean()


# In[5]:


df['Grades'].std()


# In[6]:


df['Grades'].min()


# In[7]:


df['Grades'].max()


# In[8]:


df['Grades'].quantile(.25)


# In[9]:


df['Grades'].quantile(.5)


# In[10]:


df['Grades'].quantile(.75)


# In[ ]:




