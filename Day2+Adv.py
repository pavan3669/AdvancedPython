
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

# Array of ones using matrix
array_of_ones = np.ones((3,4)) # (3,4) is (x,y) where x is no of rows and y is no of cols

array_of_ones


# In[13]:

# How to specify te data type?

# We use dtype function

array_of_ones_int = np.ones((4,5),dtype=np.int16)

array_of_ones_int


# In[15]:

#Or
array_of_ones_int = np.ones((4,5),dtype=int)

array_of_ones_int


# In[16]:

array_of_ones_bool = np.ones((4,5),dtype=bool) 

array_of_ones_bool


# In[18]:

array_of_ones_str = np.ones((3,5),dtype=str)

array_of_ones_str


# In[19]:

array_of_ones_float = np.ones((3,5),dtype=float)

array_of_ones_float


# In[20]:

array_of_ones_float1 = np.ones((3,5)) # By default it gives a float value, without declaring the data type

array_of_ones_float1


# In[21]:

array_empty = np.empty((2,3))

array_empty


# In[22]:

# How to create identity matrix

#np.eye()

array_eye = np.eye(3)

array_eye


# In[23]:

# range is in Python

# arange is in NumPy

# What is the syntax of arange

# arange(start, stop, step)

# Prob: print the list of even numbers till 20

array_of_evens = np.arange(2,20,2)

array_of_evens


# In[24]:

array_of_evens = np.range(2,20,2)

array_of_evens


# In[27]:

# It also accepts float arguments

array_of_float = np.arange(1,33,5.8)

array_of_float


# In[28]:

# Introduction to two dimentional (2D) arrays 

array_2d = np.array([(22,33,44), (42,45,11)])

array_2d


# In[29]:

# Verify shape of array

array_2d.shape


# In[ ]:

# How to create n dimetional array

# Solution: by using .reshape()


# In[31]:

array_nd = np.arange(6).reshape(3,2)

array_nd


# In[33]:

array_2d.reshape(3,2)


# In[34]:

array_nd.reshape(2,3)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



