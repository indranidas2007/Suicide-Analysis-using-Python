#!/usr/bin/env python
# coding: utf-8

# In[71]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[72]:


data= pd.read_csv(r"C:\Users\Indrani\Desktop\suicide dataset\master.csv")


# In[73]:


data


# In[74]:


data.columns


# In[75]:


data.tail()


# In[76]:


data.head()


# In[77]:


data.describe()


# In[62]:


data.isnull().sum()


# In[78]:


#Relating the variable with scatterplots (allows to infer if there's any relation between them)
sns.relplot(x="generation",y="suicides_no",data=data)


# In[79]:


sns.relplot(x="year",y="suicides_no", hue="age",data=data)


# In[80]:


sns.pairplot(data)


# In[81]:


#line plot
sns.relplot(x='year', y='suicides_no', kind='line', data=data)


# In[82]:


sns.catplot(x='year', y='suicides_no', data=data)


# In[83]:


sns.relplot(x='year', y='suicides/100k pop', kind='line', hue="age", data=data)


# In[95]:


norway_data=data[data.country=="Norway"]
norway_data


# In[97]:


Colombia_data=data[data.country=="Colombia"]
Colombia_data


# In[100]:


plt.plot(Colombia_data.year, Colombia_data.suicides_no)
plt.plot(norway_data.year, norway_data.suicides_no)
plt.legend(["Columbia","Norway"])
plt.show()


# In[ ]:




