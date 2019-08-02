
# coding: utf-8

# In[6]:

get_ipython().system('pip install numpy')


# In[5]:

get_ipython().system('pip install --upgrade pip')


# In[7]:

get_ipython().system('pip install numpy --upgrade')


# In[ ]:

# What is NumPy?
# Numpy is a numerical computing package!
# Pyhton cannot support the functionality what numpy provides directly
# Basic building block of Numpy is a powerful n dimentional array


# In[9]:

import numpy as np

array_one = np.array([1,2,3,4])

array_one


# In[10]:

number = [22,33,44,55,66]

array_two = np.array(number)

array_two


# In[11]:

# array of zeros

array_zeros = np.zeros((4,5))

array_zeros


# In[ ]:

# Source: https://www.machinelearningplus.com/python/101-numpy-exercises-python/
# Q. Import numpy as `np` and print the version number.


# In[14]:

import numpy as np

get_ipython().system('pip install numpy')


# In[15]:

#or
import numpy as np

print(np.__version__)


# In[ ]:

# Q. Create a 1D array of numbers from 0 to 9


# In[18]:

array_oneDim = np.array(range(0,10))

array_oneDim


# In[20]:

#Or

arr = np.arange(10) # arange is "array range"
arr


# In[ ]:

# Q. Create a 3×3 numpy array of all True’s


# In[37]:

array_bool = np.ones((3,3), dtype = bool) # np.ones --> Return an array of ones with shape and type of input.
array_bool


# In[38]:

np.ones(5)


# In[39]:

np.ones(1)


# In[42]:

np.ones((5,1), dtype = int) # 5x1 matrix - rows x columns


# In[43]:

np.ones((5,), dtype = int) 


# In[44]:

np.ones((2,1))


# In[45]:

s = (2,2)
np.ones(s)


# In[46]:

np.ones((5,), dtype = float) 


# In[47]:

np.ones((5,), dtype = str) 


# In[ ]:

# Q. Extract all odd numbers from arr


# In[49]:

arr = np.array([0,1,2,3,4,5,6,7,8,9])
arr


# In[50]:

arr[arr % 2 == 1]


# In[ ]:

# Q. Replace all odd numbers in arr with -1 without changing arr


# In[56]:

arr = np.arange(10)
out = np.where(arr % 2 ==1, -1, arr)
print(arr)
out


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



