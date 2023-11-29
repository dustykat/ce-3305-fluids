#!/usr/bin/env python
# coding: utf-8

# $p_2=\rho g (z_1 - \frac{V^2}{2g})$

# In[1]:


rhog = 62.4
g = 32.3
v = 16
z = 15
pressure=rhog*(z-(v**2)/(2*g))
print("pressure is",round(pressure,4),"pounds per square foot")


# In[2]:


print("pressure is",round(pressure/144,4),"pounds per square inch")


# In[ ]:




