#!/usr/bin/env python
# coding: utf-8

# Problem statement:
# It happens all the time: someone gives you data containing malformed strings,  Python, lists and missing data. How do you tidy it up so you can get on with the  analysis? 
# Take this monstrosity as the DataFrame to use in the following puzzles: 
# df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',  
# 'londON_StockhOlm', 
# 'Budapest_PaRis', 'Brussels_londOn'], 
# 'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 
# 'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]], 
# 'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', 
# '12. Air France', '"Swiss Air"']}) 
# 

# 1. Some values in the the FlightNumber column are missing. These numbers are  meant to increase by 10 with each row so 10055 and 10075 need to be put in  place. Fill in these missing numbers and make the column an integer column  (instead of a float column). 

# In[1]:


import numpy as np
import pandas as pd


# In[6]:


# Some values in the the FlightNumber column are missing. These numbers are  meant to increase by 10 

# with each row so 10055 and 10075 need to be put in  place. Fill in these missing numbers and make 

# the column an integer column  (instead of a float column)

import numpy as np
import pandas as pd

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',  
'londON_StockhOlm', 
'Budapest_PaRis', 'Brussels_londOn'], 
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]], 
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', 
'12. Air France', '"Swiss Air"']})

df


# In[7]:


df['FlightNumber']


# In[8]:


# Setting up a new index for the data frame.This index is used for the for loop iteration in the next step

newindex = np.arange(1,df.From_To.count()+1)
newindex
df.set_index(newindex, inplace = True)
df


# In[10]:


# using for loop for iteration along with isnull function to update the values for column FlightNumber

for i in np.arange(1,df.From_To.count()+1):
    if pd.isnull(df.FlightNumber.loc[i,]):
        df.loc[i,'FlightNumber'] = df.FlightNumber.loc[i - 1,] + 10
df['FlightNumber']
df


# In[11]:


# Changing the data type for FlightNumber column to integer

df['FlightNumber'].astype(int)


# 2. The From_To column would be better as two separate columns! Split each  string on the underscore delimiter _ to give a new temporary DataFrame with  the correct values. Assign the correct column names to this temporary  DataFrame. 
# 

# In[12]:


# The From_To column would be better as two separate columns! Split each  string on 

# the underscore delimiter _ to give a new temporary DataFrame with  the correct values. 

# Assign the correct column names to this temporary  DataFrame. 

df['From_To']


# In[13]:


# Creating a new temporary dataframe which is a copy of existing dataframe

df

temporarydf = df.copy()

# Splitting the column into two based on "_"

temporarydf[['From','To']] = temporarydf.From_To.str.split("_", expand = True)

# Printing new dataframe

temporarydf


# 3. Notice how the capitalisation of the city names is all mixed up in this  temporary DataFrame. Standardise the strings so that only the first letter is  uppercase (e.g. "londON" should become "London".) 

# In[14]:


# Notice how the capitalisation of the city names is all mixed up in this  temporary 

# DataFrame. Standardise the strings so that only the first letter is  uppercase (e.g. "londON" should become "London".) 

# Converting the first letter of values in 'From' column to uppercase

temporarydf.From = temporarydf.From.str.capitalize()

# Converting the first letter of values in 'To' column to uppercase

temporarydf.To = temporarydf.To.str.capitalize()

# Converting the first letter of values in 'From_To' column to uppercase

temporarydf.From_To = temporarydf.From_To.str.capitalize()

print(temporarydf)


# 4. Delete the From_To column from df and attach the temporary DataFrame  from the previous questions. 
# 

# In[15]:


# Delete the From_To column from df and attach the temporary DataFrame  from the previous questions. 

# Printing the existing df
df


# In[17]:


# Printing the data frame after deleting the "From_To" column
df.drop('From_To',axis=1,inplace=True)
df


# In[18]:


# Adding the 'From_To' column from temporary database

df['From_To'] = temporarydf['From_To']
df


# 5. In the RecentDelays column, the values have been entered into the  DataFrame as a list. We would like each first value in its own column, each 
# second value in its own column, and so on. If there isn't an Nth value, the value  should be NaN. Expand the Series of lists into a DataFrame named delays, rename the columns  delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df  with delays
# 

# In[20]:


# In the RecentDelays column, the values have been entered into the  DataFrame as a list. We would like each first value 

# in its own column, each second value in its own column, and so on. If there isn't an Nth value, the value  should be NaN.

# Expand the series of lists into a DataFrame named as delays, rename the coumns delay_1 , delay_2, etc. and 

# replace the unwanted RecentDelays column in df with delays.

# Using the original dataframe provided for this problem.

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',  
'londON_StockhOlm', 
'Budapest_PaRis', 'Brussels_londOn'], 
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]], 
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', 
'12. Air France', '"Swiss Air"']})

df
rows = []
_ = df.apply(lambda row:[rows.append([row['Airline'],row['FlightNumber'],nn,row['From_To']])
                         for nn in row.RecentDelays],axis=1)

# Printing all values in recent dealy column in separate rows

rows


# In[23]:


# Converting the data into the data frame
df_new = pd.DataFrame(rows, columns=df.columns)

# Printing existing dataframe(for comparison view)
df


# In[25]:


# Printing the revised data frame as per the criteria defined in the problem.
df_new


# In[26]:


# Expand the series of lists into a DataFrame named delays, rename the columns delay_1, delay_2,etc. and

# replace the unwanted RecentDelays column in df with delays.

# Getting the recent delay values from the data frame

df3 = pd.DataFrame(df['RecentDelays'].values.tolist())
df3


# In[35]:


length_cols = df3.shape[1]
length_cols


# In[36]:


df3.columns[0]


# In[41]:


# Creating a loop for iteration for renaming the columns

col_list = []
col_dict = {}
for i in range(length_cols):
    Key = df3.columns[i]
    #print(key,i)
    Value = "Delay" + str(i + 1)
    col_dict[Key] = Value
    
col_dict


# In[42]:


# Renaming the columns

df3.rename(columns = col_dict, inplace = True)
df3


# In[43]:


# Printing the existing data frame for comparison
df


# In[47]:


df[["Dealy1","Delay2","Delay3"]] = df3[["Delay1","Delay2","Delay3"]]


# In[48]:


# Adding the new columns to the data frame
df


# In[49]:


# Printing the revised dataframe by dropping the recent delays column as mentioned in the problem.

df.drop('RecentDelays', axis = 1, inplace = True)
df


# In[ ]:




