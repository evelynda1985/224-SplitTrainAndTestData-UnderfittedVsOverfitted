#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.model_selection import train_test_split


# In[2]:


a = np.arange(1,101)


# In[3]:


a


# In[4]:


b = np.arange(501,601)
b


# In[5]:


train_test_split(a) #the first array is the training and the second one is the test


# In[29]:


a_train, a_test, b_train, b_test= train_test_split(a, b, test_size=0.2, random_state=42) #shuffle=False in case you want the data in order


# In[30]:


a_train.shape, a_test.shape


# In[31]:


a_train


# In[32]:


a_test


# In[33]:


b_train.shape, b_test.shape


# In[34]:


b_train


# In[35]:


b_test


# In[ ]:




