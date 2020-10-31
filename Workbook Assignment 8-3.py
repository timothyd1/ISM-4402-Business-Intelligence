#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "Desktop/ISM 4402/datasets/gradedata.csv"
df = pd.read_csv(Location)


# In[6]:


plt.scatter(df["hours"], df["grade"])


# In[ ]:





# In[ ]:




