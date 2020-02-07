#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math

td=pd.read_csv('train.csv')
td.head(10)


# In[3]:



print("passanger:"+str(len(td.index)))


# In[4]:


sns.countplot(x="Survived",data=td)


# In[5]:


sns.countplot(x="Survived",hue="Sex" ,data=td)


# In[6]:


sns.countplot(x="Survived",hue="Pclass",data=td)


# In[7]:


td["Age"].plot.hist()


# In[8]:


td["Fare"].plot.hist()


# In[9]:


sns.countplot(x="SibSp",data=td)


# In[10]:


td.info()


# In[11]:


td.isnull()


# In[12]:


td.isnull().sum()


# In[14]:


sns.boxplot(x="Pclass",y="Age",data=td)


# In[17]:


td.head(5)


# In[18]:


td.drop("Cabin", axis=1, inplace=True)


# In[19]:


td.head(5)


# In[20]:


td.dropna(inplace=True)


# In[21]:


sns.heatmap(td.isnull(), yticklabels=False, cbar=False)


# In[22]:


td.isnull().sum()


# In[24]:


sns.heatmap(td.isnull(), yticklabels=False)


# In[36]:


sex = pd.get_dummies(td["Sex"],drop_first=True)
sex.head(5)


# In[37]:


td.info()


# In[41]:


embark=pd.get_dummies(td["Embarked"],drop_first=True)
embark.head(2)


# In[48]:


pcls=pd.get_dummies(td["Pclass"],drop_first=True)
pcls.head(2)


# In[55]:


td =pd.concat([td,sex,embark,pcls] ,axis=1,inplace=True)


# In[ ]:





# In[ ]:




