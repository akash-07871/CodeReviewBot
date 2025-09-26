#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


# In[ ]:




