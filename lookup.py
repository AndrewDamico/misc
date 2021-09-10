#!/usr/bin/env python
# coding: utf-8

# In[297]:


import pandas as pd


# # Create DF

# In[337]:


df = pd.DataFrame(data = {'A': ['Item 1','Item 2','Item 3'], 'B':['Item 3','Item 1','Item 2']})
df


# # Iterate through rows
# This will find the first location of the value in column A in column B, and will then return the value in column A corresponding to the row in column B

# In[340]:


for index in df.iterrows():
    df.at[index[0],'C'] = df.loc[df['B'] == df.iloc[index[0]]['A'], 'A'].values[0]


# In[341]:


df


# # An Easier Breakdown to see what is happening

# In[342]:


for index in df.iterrows():
    value_looking_for = df.iloc[index[0]]['A']
    lookup_column = df['B']
    column_to_return = 'A'
    df.at[index[0],'C'] = df.loc[lookup_column == value_looking_for, column_to_return].values[0]


# In[343]:


df


# In[ ]:




