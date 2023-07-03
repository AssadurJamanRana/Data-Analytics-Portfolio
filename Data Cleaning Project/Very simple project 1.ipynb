#!/usr/bin/env python
# coding: utf-8

# ### Importing Pandas Library

# In[1]:


import pandas as pd 


# ### Read the csv file into a pandas Dataframe

# In[2]:


data = pd.read_csv('sample.csv')


# ### Explore the dataset 

# In[3]:


data.head()


# In[4]:


data.info()


# ### Handle Missing Values

# In[5]:


data['age'].fillna(0, inplace=True)  # Replace missing age values with 0
data['email'].fillna('', inplace=True)  # Replace missing email values with an empty string
data['phone'].fillna('', inplace=True)  # Replace missing phone values with an empty string


# In[6]:


data.head()


# ### Standardize formats

# In[7]:


data['email'] = data['email'].str.lower()  # Convert email addresses to lowercase
data['phone'] = data['phone'].str.replace('-', '')  # Remove dashes from phone numbers


# In[8]:


data.head()


# In[9]:


data.info()


# ### Remove duplicates 

# In[10]:


data.drop_duplicates(subset=['email'], inplace= True)   # Remvove duplicate rows based on email column


# In[11]:


data.head()


# ### Save the cleaned data to a new CSV file

# In[12]:


data.to_csv('cleaned_sample_data.csv', index= False)


# ### More cleaning data with mean value

# In[14]:


mean_age = data[data['age'] !=0]['age'].mean()


# In[15]:


data.loc[data['age'] == 0, 'age'] = mean_age


# In[16]:


data.head()


# ### Replace null email values with name + "@example.com"

# In[17]:


data.loc[data['email'] == '', 'email'] = data['name'].str.replace(' ', '') + '@example.com'


# In[18]:


data.head()


# ### Standardize formats

# In[19]:


data['email'] = data['email'].str.lower()  # Convert email addresses to lowercase


# In[20]:


data.head()


# ### Convert 'age' column to integer

# In[21]:


data['age'] = data['age'].astype(int)


# In[22]:


data.head()


# ### Save the cleaned data to a new CSV file again

# In[23]:


data.to_csv('cleaned_sample_data_final.csv', index=False)


# In[ ]:




