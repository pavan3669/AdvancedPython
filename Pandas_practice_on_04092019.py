
# coding: utf-8

# In[3]:

import pandas as pd
import numpy as np

# Create a series with 100 random numbers

s = pd.Series(np.random.randn(100))

print(s)


# In[5]:

# Axes 

import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5))

print("The axes are:")

print(s.axes)


# In[7]:

# Empty 

import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5))

print("Is the object empty..?")

print(s.empty)


# In[8]:

# ndim - n dimentional

import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(4))

print(s)

print("The diemnsions of the object:")

print(s.ndim)


# In[9]:

# Size

import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(4))

print(s)

print("The size of the object:")

print(s.size)


# In[10]:

# Values

import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(4))

print(s)

print("The actual data series is:")

print(s.values)


# In[11]:

# Head and tail

import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(50))

print(s)

print("The first three rows of the data series:")

print(s.head(3))

print("The last three rows of the data series:")

print(s.tail(3))


# In[ ]:




# In[ ]:



