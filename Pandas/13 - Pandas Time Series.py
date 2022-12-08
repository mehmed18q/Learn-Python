#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


print (pd.to_datetime('2019-05-15 3:45pm'))


# In[3]:


pd.to_datetime('2019-05-15 3:45pm')


# In[5]:


pd.to_datetime(['2019-05-15' , '7/8/2010' , 'oct 10, 1999'])


# In[7]:


pd.to_datetime('2/25/10' , format = '%m/%d/%y')


# In[18]:


opsd_daily = pd.read_csv('opsd germany daily.csv')


# In[10]:


print(opsd_daily.shape)


# In[11]:


opsd_daily.shape


# In[12]:


opsd_daily.head()


# In[13]:


opsd_daily.tail()


# In[14]:


opsd_daily.dtypes


# In[15]:


opsd_daily = opsd_daily.set_index('Date')
opsd_daily.tail()


# In[16]:


opsd_daily.index


# In[19]:


opsd_daily = opsd_daily.set_index(pd.DatetimeIndex(opsd_daily['Date'].values))
opsd_daily


# In[20]:


opsd_daily.index


# In[21]:


opsd_daily.loc['2017-08-10']


# In[23]:


opsd_daily.loc['2017-08-10' : '2017-08-20']


# In[24]:


opsd_daily.loc['2017-08']


# In[ ]:




