#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# Load the Excel data using pd.read_csv.
ott = pd.read_csv('ott_merge.csv')

# View the columns.
print(ott.columns)


# In[3]:


# Load the CSV data using pd.read_csv.
movies = pd.read_excel('movies_merge.xlsx')

print(movies.columns)


# In[4]:


# Data imported correctly?
print(movies.head())
print(movies.shape)
print(movies.dtypes)


# In[5]:


# Data imported correctly.
print(ott.head())
print(ott.dtypes)
print(ott.shape)


# In[6]:


# Merge the two DataFrames.
mov_ott = pd.merge(movies, ott, how='left', on = 'ID')

# View the DataFrame.
print(mov_ott.shape)
mov_ott.head()


# In[7]:


# Create a simple lineplot.
sns.lineplot(x='Year', y='IMDb', data=mov_ott)


# In[8]:


# Create a simple lineplot.
sns.lineplot(x='Year', y='IMDb', data=mov_ott, ci=None)


# In[9]:


# Create lineplots with specification.
sns.lineplot(x = 'Year', y = 'IMDb',
             data=mov_ott[mov_ott['Age'].isin(['16+', '18+'])],
             hue ='Age')


# In[10]:


# Create lineplots with specification.
sns.lineplot(x = 'Year', y = 'IMDb',
             data=mov_ott[mov_ott['Age'].isin(['16+', '18+'])],
             hue ='Age', ci=None)


# In[ ]:




