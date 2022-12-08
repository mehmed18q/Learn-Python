#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("opsd germany daily.csv")
df


# In[3]:


print(df.info())


# In[4]:


print(df.head())


# In[5]:


print(df.describe())


# In[6]:


print("Average Consumption: ", df['Consumption'].mean())


# In[7]:


print("Standard Deviation in Consumption: ", df['Consumption'].std())


# In[11]:


print("Correlation between Solar and Wind : ")
df['Solar'].corr(df['Wind'])


# In[13]:


print("Minimum Power Quantity: " , df['Wind+Solar'].min())
print("Maximum Power Quantity: " , df['Wind+Solar'].max())


# In[ ]:


# mode() , var() ,cov() , median() , ...

